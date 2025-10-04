import numpy as np
from scipy.special import softmax




def create_first_time(features_vectors:np.array, chocies:list[bool]) -> np.array:
    VECTOR_FEATURES = 8


    assert len(features_vectors) == len(chocies)
    
    sum = np.zeros(VECTOR_FEATURES)

    for idx, choice in enumerate(chocies):
        if choice == False:
            features_vectors[idx] = (-1)*features_vectors[idx]

        sum += features_vectors[idx]

    return softmax(sum)


def update_preferences(user_preferences: np.array, place_features: np.array, decision: bool) -> dict:
    LR = 0.01
    FEATURE_NAMES = ["orientality", "temperature", "historicity", "sportiness","forest_cover","build_up_area","terrain_fluctuation", "water"]
    RANDOM_PARM_COUNT = 3
    num_features = len(user_preferences)

    assert len(user_preferences) == len(place_features)

    direction = 1
    if not decision:
        direction *= -1


    user_preferences = np.clip(user_preferences + LR*direction*(place_features-user_preferences),0,1)

    #Chosing Random Fetures for DataBase part
    indexes = np.random.choice(np.arange(num_features), size=(RANDOM_PARM_COUNT), replace=False)

    samples = {}
    for i in indexes:
        samples[FEATURE_NAMES[i]] = float(user_preferences[i])

    return samples

