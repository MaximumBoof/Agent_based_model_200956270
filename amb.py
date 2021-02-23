# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:35:15 2021

 

@author: Stephen
"""

import random
import operator 
import matplotlib.pyplot
import time

#Adding seeds means you can get the same 'randomness' each time making debugging easier
#The seed can be linked to clock time, so you can debug easier with the whole log
seed = 6
random.seed(seed)

# Start timer
# Used to optimise the code
    # But you should really remove print stuff because that can take awhile
start_time = time.process_time()
 

def distance_between(agents_row_a, agents_row_b):
     return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

 

num_of_agents = 3
number_of_iterations = 3
agents = []


# Make the agents
for i in range(num_of_agents):
        agents.append([random.randint(0,100),random.randint(0,100)])
        
print (agents)

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
            
    print ("agents", agents)

# Using matplot to create a plot
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show() 

# Below is my orginal attempt
# It illustrates the big difference in where the print is placed
# If placed at the end you get a 0
#If placed with an indent it gives out a number with each agent, which is what I want

# for agents_row_a in agents:
#     for agents_row_b in agents:
#         distance = distance_between(agents_row_a, agents_row_b)
#         print(distance)
#         print(agents_row_a)
#         print(agents_row_b)
# print(distance)


# Important to note with the below is that you can reuse the same i/j etc
# In this case, we didn't reuse j because it makes it more clear because it is refering to something else
# for i in range(num_of_agents):
#     for k in range(i):
#             distance = distance_between(agents[i], agents[k])
#             print(distance)
#             print(i, agents[i])
#             print(k, agents[k])

# Using the if below leads to only the distances being shown once
    # Removing the duplicates like distance between a and b + b and a
# Also, of interest is the how it takes longer to compute this than just putting all the distane values
for i in range(num_of_agents):
    for k in range(num_of_agents):
        if (i < k):
            distance = distance_between(agents[i], agents[k])
            print("distance", distance)
            print(i, agents[i])
            print(k, agents[k])

# Important to note where the print indentation is

end_time = time.process_time()

print("total time", end_time - start_time)