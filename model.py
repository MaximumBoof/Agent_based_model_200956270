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

num_of_agents = 2
num_of_iterations = 10
agents = []
environment = []


f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist= [] 
    for values in row:
        rowlist.append(values)
    environment.append(rowlist)
        
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5

# Make the agents.
for i in range(num_of_agents):
     agents.append(agentframework.Agent())
     print("SP", agents[i].x, agents[i].y)

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        print("IT", agents[i].x, agents[i].y)
        
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 
