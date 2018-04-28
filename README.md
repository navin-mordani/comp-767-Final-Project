
# comp-767-Final-Project
## environments.py
### EnvSetTarget 
```
Environment for Agent 1 that sets the target. The aim of agent 1 is to maximize the score(target).
```
#### State Space 

Num | Observation | Min | Max
---|---|---|---
0 | time_steps_elapsed(number of darts thrown so far) | 0 | max_time_steps_elapsed set by the user
1 |  lives_lost | 0 | max_lives_lost set by the user 



#### Action Space

Action Number | Max Reward associated| Prob. of success
------------ | -------------|--------------
0 | 1 | 0.95
1 | 2 | 0.88
2 | 4 | 0.80
3 | 6 | 0.6


#### Reward
On every action if the action successful then the maximum reward associated
with the action will be achieved else a reward of  will be achieved.\
For example: on action 0 the max reward associated is 1. So if the action was successful then reward of 1 will be achieved else 0 will be achieved.

#### Start state
At the start no time steps have elapsed so far ,i.e no darts have been thrown yet. Therefore the number of time_steps_elased = 0.\
Similarly no lives have been lost so far. Therefore, the lives_lost = 0.

Start state: [0,0] 

#### Episode Termination
The episodes terminates if either of this happens:-\
* The time is over. That is the time_steps_elapsed becomes equal to max_time_steps elapsed that was set by the user
when creating the environment. (Ins short you have ran out of darts)
* All the lives have been lost. That is the variable lives_lost becomes equal to the max lives that the user had set 
when creating the environment.

For example if the env was initiated with max time steps = 6, and max lives = 2 then all states [6,-] and [-,2] are terminal states.




```

### EnvChaseTarget
```
Environment for Agent 2 that chases the target. The aim of agent 2 is to achieve the target.
```
#### State Space 

Num | Observation | Min | Max
---|---|---|---
0 | time_steps_elapsed(number of darts thrown so far) | 0 | max_time_steps_elapsed set by the user
1 |  lives_lost | 0 | max_lives_lost set by the user 
2 | distance_from_target | -5 | target


#### Action Space

Action Number | Max Reward associated| Prob. of success
------------ | -------------|--------------
0 | 1 | 0.95
1 | 2 | 0.88
2 | 4 | 0.80
3 | 6 | 0.6

#### Reward
A reward of +1 is achieved if the target is achieved. And if by the end of the episode the target is not achieved then a reward of -1
is given. Hence, only on reaching the terminal states a non-zero reward is achieved.

#### Start state
At the start no time steps have elapsed so far ,i.e no darts have been thrown yet. Therefore the number of time_steps_elased = 0.\
Similarly no lives have been lost so far. Therefore, the lives_lost = 0.\
The distance from the target is the target itself as no points are scored to move towards the target.

Start state: [0,0,target] 

#### Episode Termination
The episodes terminates if either of this happens:-\
* Distance from the target becomes less than or equal to 0.
* The time is over. That is the time_steps_elapsed becomes equal to max_time_steps elapsed that was set by the user
when creating the environment. (Ins short you have ran out of darts)
* All the lives have been lost. That is the variable lives_lost becomes equal to the max lives that the user had set 
when creating the environment.

For example if the env was initiated with max time steps = 6, max lives = 2, target=10 then all states [6,-,-], [-,2,-] and [-,-,<=0] are terminal states.

##Methods
```
###Agent 1
The learning methods for agent 1 can be found in the file agent_1_learning.ipynb
```
```
###Agent 2 
The actor critic learning method can be found in the file actor_critic_second_agent.ipynb
```
##Requirements
```
requirements.txt
``` 
