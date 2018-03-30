import numpy as np
from environments import EnvSetTarget

"""
How to use the environment
"""

#this makes new environment. This initializes state to [0,0]
env = EnvSetTarget()

# this resets state to [0,0]
env.reset()

#to teleport to a new state
env.set([100,2])

#to take action
action = 1
observation, reward, done, info = env.step(action)