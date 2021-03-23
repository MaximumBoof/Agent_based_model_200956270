# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:38:10 2021

@author: Stephen
"""
import random

seed = 6
random.seed(seed)

class Agent ():
    def __init__ (self, environment, agents):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0

    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 
    
    def distance_between(self, agents):
        return (((self.x - self.x)**2) +
            ((self.y - self.y)**2))**0.5
    
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                sum = self.store + agent.store
                average = sum /2
                self.store = average
                agent.store = average
                #print("sharing " + str(distance) + " " + str(average))
       
    