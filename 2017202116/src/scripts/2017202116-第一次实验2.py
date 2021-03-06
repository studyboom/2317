#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import gym
weigth=np.ones(4)+np.random.rand(4)#[50.4,90.2,106.2,80]#
weight_best=np.ones(4)#[50.4,90.2,106.2,80]#
change_alpha=1
score_best=0
env = gym.make('CartPole-v1')
env.seed(1)     # reproducible, general Policy gradient has high variance
env = env.unwrapped

for i_episode in range(3000):
    weigth = weight_best
    observation = env.reset()
    score=0
    print("times:",i_episode,'score_best',score_best)
    weigth += np.random.rand(4) * change_alpha
    while True:
        env.render()
        action = np.sum(np.multiply(weigth, observation))
        if action>0:
            action =1
        else:
            action =0
        observation_, reward, done, info = env.step(action)
        score+=reward
        if done:
            if score > score_best:
                score_best = score
                weight_best = weigth
                change_alpha *= 0.5
            else:
                change_alpha *= 2
            break
        if score>500 and np.sum(np.abs(weight_best-weigth))<0.001:
            print("best",score,"episode",i_episode,"w:",weight_best)
        observation = observation_
env.close()

