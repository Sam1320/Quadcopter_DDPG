# Teach a Quadcopter to fly with DDPG actor-critic agent

<img src="https://github.com/Sam1320/Quadcopter_DDPG/blob/master/drone.jpg" height="150">

Deep Reinforcement Learning project for Udacity's [Machine Learning Engineer](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t)

## Description

I designed a reinforcement learning task for flying a quadcopter in a simulated environment, and built an agent that autonomously learned to perform the task.

- My agent had to learn how to best manage the quadcopter's four points of thrust in order to accumulate more reward specified by the learning task.

- The goal that I specified for the agent was to take off and find the fastest path to a specific area of the environment.

- This involved my crafting a straightforward reward function that would incentivize an agent to first avoid crashing, and then approximate the target area.

- The algorithm the agent used to solve the task was DDPG  [(deep deterministic policy gradient Lillicrap, Timothy P., et al.)](https://arxiv.org/pdf/1509.02971.pdf) which is a model-free actor-critic method where the underlying policy is deterministic and external noise is added to create exploratory behavior.

## Agent & Task
* [DDPG Agent](https://github.com/Sam1320/Quadcopter_DDPG/blob/master/agents/DDPG.py) 
* [Actor & Critic Models](https://github.com/Sam1320/Quadcopter_DDPG/blob/master/agents/models.py)
* [Replay Buffer & Noise functions](https://github.com/Sam1320/Quadcopter_DDPG/blob/master/agents/helpers.py)
* [Task](https://github.com/Sam1320/Quadcopter_DDPG/blob/master/task.py)

## Completed Project and Evaluation
* [Project Notebook](https://github.com/Sam1320/Quadcopter_DDPG/blob/master/Quadcopter_Project.ipynb)
* [Review](https://github.com/Sam1320/Quadcopter_DDPG/blob/master/Project_Review.pdf)
