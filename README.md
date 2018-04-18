# comp-767-Final-Project
## environments.py
### EnvSetTarget 
```
Environment for Agent 1 that sets the target. The aim of agent 1 is to maximize the score(target).
```
####State Space 

Num | Observation | Min | Max
---|---|---|---
0 | time_steps_elapsed(number of darts thrown so far) | 0 | max_time_steps_elapsed set by the user
1 |  lives_lost | 0 | max_lives_lost set by the user 



* **Action Space**

Action Number | Max Reward associated| Prob. of success
------------ | -------------|--------------
0 | 1 | 0.95
1 | 2 | 0.88
2 | 4 | 0.80
3 | 6 | 0.6


* **Reward**
On every action if the action successful then the maximum reward associated
with the action will be achieved else a reward of  will be achieved.
For example: on action 0 the max reward associated is 1. So if the action was successful then reward of 1 will be achieved else 0 will be achieved.

* **Start state**
At the start no time steps have elapsed so far ,i.e no darts have been thrown yet. Therefore the number of time_steps_elased = 0.

```
