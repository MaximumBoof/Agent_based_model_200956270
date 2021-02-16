# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:35:15 2021

@author: Stephen
"""

import random
import operator 
import matplotlib.pyplot

num_of_agents = 10
number_of_iterations = 100

#This creates an empty list
agents = []

# Make the agents
for i in range(num_of_agents):
        agents.append([random.randint(0,100),random.randint(0,100)])

# Move the agents
for j in range(number_of_iterations):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
            
print (agents)

# This max function will give the coordinates with the largest y value
print(max(agents))    
# However, if we want to show the coordinates with the largest x value, we have to import operator functions
print(max(agents, key=operator.itemgetter(1)))  

# Calculate Eudclian distance between the points (Using pythagoras)
# Define difference in y and x
dy = agents[0][0]-agents[1][0]
dx = agents[0][1]-agents[1][1]

# Pythogras
distance = ((dy**2)+(dx**2))**0.5

print (distance)

# Using matplot to create a plot

matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])