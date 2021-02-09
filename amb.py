# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:35:15 2021

@author: Stephen
"""

import random

# Set up variables (in this case coordinates) for a first object or point 
y0 = random.random() * 100
x0 = random.random() * 100 

# Random walk step one
# For object 1 coordinates
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

# Random walk step two
# For object 1 coordinates
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
    
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