## User
User as individual person have some preferences, so trips advices *(not always)* will be profiled.
Let`s se how.
### Create personal profile
First algorithm will determine best user preferences  (details 1.)

### Create new trip
Second algorithm works as follows (details in 2.):
 - randomly choose seed ex. ```[0.32, ... , 0.97]``` and thanks to user response "swipe" will establish best 
destination for him (I)
 - due to randomly sampled user preferences will update his "trip preferences" and establish best destination
   (II)

### Algorithm details
1. This algorithm base on naive bayes random sampling destinations for user.
- At first we set all features to `{1., ..., 1.}` so probability of choosing each one is equal to `1 \ num_features`
- Next due to user response algorithm change probabilities as follows:
  - a