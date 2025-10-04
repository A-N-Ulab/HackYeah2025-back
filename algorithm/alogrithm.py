import numpy as np
from scipy.special import softmax




def create_first_time(features_vectors:np.array, chocies:list[bool]):
    VECTOR_FEATURES = 8


    assert len(features_vectors) == len(chocies)
    
    sum = np.zeros(VECTOR_FEATURES)

    for idx, choice in enumerate(chocies):
        if choice == False:
            features_vectors[idx] = (-1)*features_vectors[idx]

        sum += features_vectors[idx]

    return softmax(sum)


def create_trip(user_preferences: np.array, random: bool = False) -> np.array:
    num_of_parameters = len(user_preferences)

    if random:
        return np.random.random(num_of_parameters)

    random_parameter_difference = (np.random.random(num_of_parameters) - 1) * 0.01
    user_preferences = user_preferences + random_parameter_difference
    user_preferences = np.clip(user_preferences, 0, 1)

    return user_preferences

def update_preferences(user_preferences: np.array, place_features: np.array, decision: bool) -> np.array:
    learning_rate = 0.01
    num_features = 3
    num_of_parameters = 10

    chosen_features = np.zeros(num_of_parameters)
    indices = np.random.choice(num_of_parameters, num_features, replace=False)
    chosen_features[indices] = learning_rate



    if decision:
        pass

    return user_preferences

    # update




def update_trip():
    pass

