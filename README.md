# comp-767-Final-Project
## environments.py
### EnvSetTarget 
```
Environment for Agent 1 that sets the target. The aim of agent 1 is to maximize the score(target).
```
* **State Space** 

Num | Observation | Min | Max
---|---|---|---
0 | time_steps_elapsed(number of darts thrown so far) | 0 | max_time_steps_elapsed set by the user
1 |  lives_lost | 0 | max_lives_lost set by the user 


--------------
* **Action Space**

Action Number | Max Reward associated| Prob. of success
------------ | -------------|--------------
0 | 1 | 0.95
1 | 2 | 0.88
2 | 4 | 0.80
3 | 6 | 0.6
```
