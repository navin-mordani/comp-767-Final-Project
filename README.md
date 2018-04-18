# comp-767-Final-Project
## environments.py
### EnvSetTarget 
```
Environment for Agent 1 that sets the target. The aim of agent 1 is to maximize the score(target).
```
* **State Space** 

Num | Observation | Min | Max
---|---|---|---
0 | time_steps_elapsed(number of darts thrown so far) | 0 | 6
1 |  lives_lost | 0 | 2

[//] : # (Two variables :-)
[//] : # (1. time_steps_elapsed(number of darts the agent has thrown so far) lies in the set[0,..,120])
[//] : # (2. lives_lost(number of darts that have missed the boards they were aimed at) lies in the set[0,..,10])
--------------
* **Action Space**

Action Number | Max Reward associated| Prob. of success
------------ | -------------|--------------
0 | 1 | 0.95
1 | 2 | 0.88
2 | 4 | 0.80
3 | 6 | 0.6
```
