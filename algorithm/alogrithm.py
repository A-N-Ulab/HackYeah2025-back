import numpy as np


def create_first_time():
    return np.zeros(10)


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

