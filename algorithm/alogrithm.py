import numpy as np
from scipy.special import softmax


FEATURE_NAMES = ["orientality", "temperature", "historicity", "sportiness","forest_cover","build_up_area","terrain_fluctuation", "water"]
NUM_FEATURES = len(FEATURE_NAMES)
LR = 0.01
RANDOM_PARM_COUNT = 3

#For Backend
def _make_dict(values:np.array) -> dict:
    values = map(float, values)
    return dict(zip(FEATURE_NAMES, values))


#Algorithm
def create_first_time(features_vectors:list[list[float]], choices:list[bool]) -> dict:
    assert len(features_vectors) == len(choices)

    for features_of_dest in features_vectors:
        assert len(features_of_dest) == NUM_FEATURES
    
    features_vectors = np.array(features_vectors)

    sum = np.zeros(NUM_FEATURES)

    for idx, choice in enumerate(choices):
        if choice == False:
            features_vectors[idx] = (-1)*features_vectors[idx]

        sum += features_vectors[idx]

    return _make_dict(softmax(sum))

def sampler() -> list[str]:
    #Chosing Random Fetures for DataBase part
    indexes = np.random.choice(np.arange(NUM_FEATURES), size=(RANDOM_PARM_COUNT), replace=False)

    samples = []
    for i in indexes:
        samples.append(FEATURE_NAMES[i])
    
    return samples

def update_preferences(user_preferences: list[float], place_features: list[float], decision: bool) -> dict:
    assert len(user_preferences) == len(place_features) == NUM_FEATURES

    user_preferences = np.array(user_preferences)
    place_features = np.array(place_features)

    direction = 1
    if not decision:
        direction *= -1

    user_preferences = np.clip(user_preferences + LR*direction*(place_features-user_preferences),0,1)


    return _make_dict(user_preferences)

