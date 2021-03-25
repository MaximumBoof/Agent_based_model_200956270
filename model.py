# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:18:37 2021

@author: Stephen
"""

import random
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv

seed = 2
random.seed(seed)

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
environment = []
agents = []

#Part of the animation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#Importing the CSV
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
     #print("SP", agents[i].x, agents[i].y)

def update(frame_number): 
    fig.clear()    
    # Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
        #The random is to randomise the order which the agents are processed for each iteration (not sure if I've done it right)
            random.shuffle(agents)
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
    
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
   
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        
        matplotlib.pyplot.imshow(environment)
        matplotlib.pyplot.xlim(0, 99)
        matplotlib.pyplot.ylim(0, 99)

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()

