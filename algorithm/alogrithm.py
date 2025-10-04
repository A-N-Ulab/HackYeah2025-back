import numpy as np


def create_first_time():
    return np.zeros(10)



def create_trip(user_preferences: np.array, random: bool = False) -> np.array:
    if random:
        return np.random.random(10)
    #TODO create_trip algo
    random_vector = np.random.randn(10)
    return np.zeros(10)

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

