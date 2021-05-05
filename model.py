# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:18:37 2021

@author: Stephen
"""
#------------- Start of imports
import random
import matplotlib
matplotlib.use('TkAgg')
import tkinter 
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import requests
import bs4
#------------ End of imports

#------------ Defining functions
# For each each frame in animation, allows the agents to move, eat and share for each iteration used within the animation.
def update(frame_number): 
    fig.clear()
    global carry_on
    # Allows the agents to move, eat and share with each iteration.
    for i in range(num_of_agents):
        # The random.shuffle randomises the order which the agents are processed for each iteration.
        # This prevents the first agent always moving and eating before the other agents.
            random.shuffle(agents)
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
    
    # Creating a stopping conditions, where all the agents must have at least 1000 within their store.
    carry_on = False
    for agent in agents:
        if agent.store < 1000:
            carry_on = True
    if (carry_on==False):
        print("early stopping condition met after " + str(frame_number)+ " iterations")
    # Agents are given their x/y positions and colours
    # Without the colour being attached to the agent here, the colours would shuffle with each iteration due to the shuffle above.
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y,c=agents[i].colour)
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    
# Used within the animation
def gen_function(b = [0]):
    a = 0
    global carry_on # Not actually needed as we're not assigning, but clearer
    #while (a < 10) & (carry_on) :
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
# Function which runs the model
# This is called when the GUI 'run' button is pressed
def run():
    # To allow the model to be run multiple times with differing variables, without closing down the window, the agents and environment need to be cleared.
    # Otherwise, the agents will be appened with the new value, meaning there will be more agents than actually appear, so they wouldn't move correctly.
    agents.clear()
    #environment.clear()
    global environment
    environment=import_csv()
    # Gets the three user defined values from the GUI spinboxes.
    global num_of_iterations
    num_of_iterations = int(noit.get())
    print("Iterations = "+ noit.get())
    global num_of_agents
    num_of_agents = int(noag.get())
    print("Agents = " + noag.get())
    global neighbourhood
    neighbourhood = int(neigh.get())
    print("Neighbourhood = " + neigh.get())
    # Make the agents with x/y values from the web scraped data
    for i in range(num_of_agents):
           y = int(td_ys[i].text)
           x = int(td_xs[i].text)
           # Generating a 6 digit hexidecimal number to assign a colour to each agent.
           # Without this, the colour of each agent changes because of random.shuffle in the update function.
           hex_number = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
           agents.append(agentframework.Agent(environment, agents, x, y, hex_number ))
   # global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)    
    print("2",len(agents))
    canvas.draw()

# A function which which quits the window and stops the model from running.
def exiting():
    root.quit()
    root.destroy() 
#---------- End of functions

# Pulling in data from a html page
# This data is x and y values, used as the starting locations of the agents
# This data request section can take 30 seconds to complete
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
    


# A seed is used throughout testing to maintain consistency when testing
seed = 1
random.seed(seed)

# Creating a lists for the environment and agents
environment = []
agents = []

# Importing the CSV file, used to create the environment
# returns numeric array of data to form background
def import_csv():
    environment_info=[]
    f = open('in.txt', newline='')
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

    for row in reader:
        rowlist= [] 
        for values in row:
            rowlist.append(values)
        environment_info.append(rowlist)
    return environment_info
    
carry_on = True	

# Creating the GUI, with a simple title
root = tkinter.Tk() 
root.wm_title("Model - 200956270")

# Creates a figure and adds axes used when animating
fig = matplotlib.pyplot.figure()
ax = fig.add_axes([0, 0, 1, 1])

# Creating frames for placing GUI parts, such as spinboxes and the animation
leftframe= tkinter.Frame(root)
leftframe.pack(side=tkinter.LEFT)
animationframe = tkinter.Frame(root)
animationframe.pack(side=tkinter.RIGHT)

# Adding number of iterations label and spinbox, on the left frame of the window
noitlab = tkinter.Label(leftframe, text ='No. of iterations', fg="navyblue",font = "50")
noit = tkinter.Spinbox(leftframe, from_= 1, to = 1000) 
noitlab.grid(row=1,column=0, sticky=tkinter.W)
noit.grid(row=2,column=0, sticky=tkinter.W)

# Adding number of agents label and spinbox, on the left frame of the window
noaglab = tkinter.Label(leftframe, text ='No. of agents', fg="navyblue",font = "50") 
noag = tkinter.Spinbox(leftframe, from_= 1, to = 100) 
noaglab.grid(row=3,column=0,sticky=tkinter.W)
noag.grid(row=4,column=0,sticky=tkinter.W)

# Adding neighbourhood label and spinbox, on the left frame of the window
neighlab = tkinter.Label(leftframe, text ='Neighbourhood size', fg="navyblue",font = "50") 
neigh = tkinter.Spinbox(leftframe, from_= 1, to = 100) 
neighlab.grid(row=5,column=0,sticky=tkinter.W)
neigh.grid(row=6,column=0,sticky=tkinter.W)

# Adding a button to run the model, rather than the drop down menu
# This is more intuative with the addition of spinboxes for variables
r = tkinter.Button(leftframe, text ='Run model', fg="navyblue",font = "50", command=run)
r.grid(row=7,column=0,sticky=tkinter.W, ipady=5)

# Adding a button to exit the window and stop the model
r = tkinter.Button(leftframe, text ='Exit window', fg="navyblue",font = "50", command=exiting)
r.grid(row=8,column=0,sticky=tkinter.W, ipady=5)

# Locating in the window where the animation will be
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=animationframe)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# This stops the model running when figure window is exited.
# Without this, when you exit the window, the model can still be running, preventing you from running a new instance of the model.
root.protocol('WM_DELETE_WINDOW', exiting)

tkinter.mainloop() # Wait for interactions. 