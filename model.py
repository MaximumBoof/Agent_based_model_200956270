# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:18:37 2021

@author: Stephen
"""

import random
import matplotlib.pyplot
import agentframework
import csv

seed = 2
random.seed(seed)

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
environment = []
agents = []

f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist= [] 
    for values in row:
        rowlist.append(values)
    environment.append(rowlist)

# Make the agents.
for i in range(num_of_agents):
     agents.append(agentframework.Agent(environment, agents))
     print("SP", agents[i].x, agents[i].y)

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        #The random is to randomise the order which the agents are processed for each iteration (not sure if I've done it right)
        random.shuffle(agents)
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

for i in range(num_of_agents):
    print("EP", agents[i].x, agents[i].y)
        
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

