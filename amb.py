# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:35:15 2021

@author: Stephen
"""

import random

#This creates an empty list
agents = []

# Set up variables (in this case coordinates) for a first object or point 
y0 = random.random() * 100
x0 = random.random() * 100 

# Add the first set of coordinates to the list but because of the extra square brackets, this is adding a list in a list
# We have a two dimensional dataset, in which the first dimension agents[0] represents each agent, and the second dimension is the two coordinates, so agents[0][0] is the y coordinate and agents[0][1] is the x coordinate. As we only have one set of coordinates so far, if you print(agents) you should see something like this (though the numbers will be different):
agents.append ([y0, x0])

print (agents)

# Random walk step one
# For object 1 coordinates
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

# Random walk step two
# For object 1 coordinates
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
    
# Set up variables (coordinates in this case) for a new object or point
x1 = random.random() * 100
y1 = random.random() * 100

# Random walk step one
# For object 2 coordinates
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

# Random walk step two 
# For object 2 coordinates
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1
    
print (y0, x0, y1, x1)

# Calculate Eudclian distance between the points (Using pythagoras)
# Define difference in y and x
dy = y0-y1
dx = x0-x1

# Pythogras
distance = ((dy**2)+(dx**2))**0.5

print (distance)