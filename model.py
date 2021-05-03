# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:18:37 2021

@author: Stephen
"""

import random
import matplotlib
#from matplotlib.figure import Figure
matplotlib.use('TkAgg')
import tkinter 
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

def update(frame_number): 
    fig.clear()
    global carry_on
    # Move the agents.
    #for j in range(num_of_iterations):
    
    for i in range(num_of_agents):
        #The random is to randomise the order which the agents are processed for each iteration (not sure if I've done it right)
            random.shuffle(agents)
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
    

    carry_on = False
    for agent in agents:
        if agent.store < 1000:
            carry_on = True
    if (carry_on==False):
        print("early stopping condition met after " + str(frame_number)+ " iterations")
            
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y,c=agents[i].colour)
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    #while (a < 10) & (carry_on) :
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
    
        
def run():
    global num_of_iterations
    num_of_iterations = int(noit.get())
    print("Iter"+ noit.get())
    global num_of_agents
    num_of_agents = int(noag.get())
    print("Ag" + noag.get())
    # Make the agents.
    for i in range(num_of_agents):
      agents.append(agentframework.Agent(environment, agents,colourArray[i]))
   # global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)    
    canvas.draw()

def exiting():
    root.quit()
    root.destroy()
    #sys.exit(0)
    
root = tkinter.Tk() 
root.wm_title("Model")

seed = 1
random.seed(seed)

# num_of_agents = 10
# num_of_iterations = 1000
neighbourhood = 10
environment = []
agents = []




#Importing the CSV
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist= [] 
    for values in row:
        rowlist.append(values)
    environment.append(rowlist)
    
carry_on = True	
colourArray = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
# # Make the agents.
# for i in range(num_of_agents):
#      agents.append(agentframework.Agent(environment, agents,colourArray[i]))
     #print("SP", agents[i].x, agents[i].y)
        
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)    


menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

# w = tkinter.Label(root, text ='StudyTonight', fg="navyblue",font = "50") 
# w.pack() 




#Part of the animation
fig = matplotlib.pyplot.figure()
ax = fig.add_axes([0, 0, 1, 1])
# canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
#canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 
# pack_toolbar=False will make it easier to use a layout manager later on.

leftframe= tkinter.Frame(root)
leftframe.pack(side=tkinter.LEFT)

nextframe =tkinter.Frame(root)
nextframe.pack(side=tkinter.BOTTOM)

animationframe = tkinter.Frame(root)
animationframe.pack(side=tkinter.RIGHT)

noitlab = tkinter.Label(leftframe, text ='No. iterations', fg="navyblue",font = "50")
# w.place(y=10, x=0)
noit = tkinter.Spinbox(leftframe, from_= 1, to = 1000)
# sp.place(x=0, y=0) 

noitlab.grid(row=0,column=0, sticky=tkinter.W)
noit.grid(row=1,column=0, sticky=tkinter.W)

noaglab = tkinter.Label(leftframe, text ='No of agents', fg="navyblue",font = "50") 
noag = tkinter.Spinbox(leftframe, from_= 1, to = 100) 

noaglab.grid(row=3,column=0,sticky=tkinter.W)
noag.grid(row=4,column=0,sticky=tkinter.W)

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=animationframe)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

root.protocol('WM_DELETE_WINDOW', exiting)

tkinter.mainloop() # Wait for interactions. 