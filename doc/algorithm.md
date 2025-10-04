# Algorithm

## Functions and types
Algorithim is based on three functions.

### Initializations
```python
def create_first_time(features_vectors:list[list[float]], choices:list[bool]) -> dict
```
That create new user preferences basing on first **n** accepted or rejected places.

### Updating
```python
update_preferences(user_preferences: list[float], place_features: list[float], decision: bool) -> dict:
```
That is updating user preferences basing on a last user decision.


### Sampler
```python
def sampler() -> list[str]:
```
That Samples **k** random features to define decision plane

## How it works
User as individual person have some preferences. The main idea is to find the closest to user destination place.

### Create personal profile
First algorithm will determine best user preferences basing on quick **Swipe&GO** session. 

### Choosing a next destination
The next destination will be the closest, not swiped while current session, neighbour on the randomly generated decision plane.

### Updating a user preferences
While being given new destination the user preferences will update accordingly to user Swipe.


