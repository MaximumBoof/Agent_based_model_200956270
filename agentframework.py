# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:38:10 2021

@author: Stephen
"""
import random

seed = 6
random.seed(seed)

class Agent ():
    def __init__ (self):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        
        print("SP", self.x, self.y)

    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
        print("EP", self.x, self.y)

    