# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:38:10 2021

@author: Stephen
"""
import random

seed = 6
random.seed(seed)
# Creating an agent class
class Agent ():
    def __init__ (self, environment, agents, x, y, colour):
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.colour=colour
        #Ensuring the model still runs even if it can't pull the data
        if (x==None):
            self.x = random.randint(0,99) 
        else:
            self.x = x
        if (y==None):
            self.y = random.randint(0,99)
        else:
            self.y = y
    
    # The function which dictates which direction all the agents move in, depending on whether a random number is above or below 0.5.
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
    # A function which allows the agents to eat part of the environment, if the environment where they are has a value above 10. 
    # Eating removes 10 from the environment function and the agent gains 10 in their storage.       
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 
  
    # A function which measures the distance between an agent and all other agents.
    # The formula used is pythagoras based.
    # This is required for the sharing function.
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
             
   # This function allows agents to share their store if they are within the user defined neighbourhood distance between eachother. 
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                sum = self.store + agent.store
                average = sum /2
                self.store = average
                agent.store = average
       
    