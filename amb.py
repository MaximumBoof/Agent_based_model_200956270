# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:35:15 2021

@author: Stephen
"""

import random

#This creates an empty list
agents = []

# Add the first set of coordinates to the list but because of the extra square brackets, this is adding a list in a list
# We have a two dimensional dataset, in which the first dimension agents[0] represents each agent, and the second dimension is the two coordinates, so agents[0][0] is the y coordinate and agents[0][1] is the x coordinate. As we only have one set of coordinates so far, if you print(agents) you should see something like this (though the numbers will be different):
agents.append([random.randint(0,99),random.randint(0,99)])

print (agents)

# Random walk step one
# For object 1 coordinates
if random.randint(0,99) < 50:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
if random.randint(0,99) < 50:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

# Random walk step two
# For object 1 coordinates
if random.randint(0,99) < 50:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
if random.randint(0,99) < 50:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
    
# Added another set of coordates for the second age
agents.append([random.randint(0,99),random.randint(0,99)])

# Random walk step one
# For object 2 coordinates
if random.randint(0,99) < 50:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
if random.randint(0,99) < 50:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

# Random walk step two 
# For object 2 coordinates
if random.randint(0,99) < 50:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
if random.randint(0,99) < 50:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
    
# Calculate Eudclian distance between the points (Using pythagoras)
# Define difference in y and x
dy = agents[0][0]-agents[1][0]
dx = agents[0][1]-agents[1][1]

# Pythogras
distance = ((dy**2)+(dx**2))**0.5

print (distance)