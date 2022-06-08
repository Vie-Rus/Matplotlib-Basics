# Matplotlib Basics - written by V I E R U S
# June 7, 2022
# If not already install matplotlib with 'pip install matplotlib' and 'pip install numpy' with cmd
# This program goes into the basics of matplotlib Pie Charts

# Create pie chart, labels,wedge at 90 degrees, explode, shadow, legend, color

#----------------------------------------------------------------------------------------------
#Imports
from matplotlib import *
import matplotlib.pyplot as mplt
import numpy as np


#Pie Chart-----------------------------------------------------------------------------------------
#Pie Plots------------------------------------
    #num1
pieChart = np.array([25,15,50,3,7])                         #values, Doesn't need to equal 100

#Pie Plots END--------------------------------

    #Created a pie chart
mplt.pie(pieChart)                                          #add values to piechart
mplt.title('Created Pie Chart')                             #Add title
mplt.show()                                                 #Create GUI pie Chart


    #Labels
pieLabels = ["A", "B", "C", "D", "E"]                       #Assign Labels to values
mplt.pie(pieChart, labels=pieLabels)                        #Add labels to values
mplt.title('Labels')
mplt.show()


    #First Wedge at 90 Degree
mplt.pie(pieChart, startangle=90)                           #Starts creating values at the 90 degrees then around
mplt.title('90 Degrees')
mplt.show()


    #Explode
pieEx = [0.2,0,0,0,0]                                       #remove a piece of the pie by .2
mplt.pie(pieChart, explode=pieEx)                           #Add explode to pie
mplt.title('Exploded')
mplt.show()


    #Shadow
pieEx = [0.2,0,0,0,0]
mplt.pie(pieChart, explode=pieEx, shadow= True)             #Add a shadow to pie, explode helps to see it better
mplt.title('With Shadow')
mplt.show()


    #Legend
pieLabels = ["A", "B", "C", "D", "E"]
mplt.pie(pieChart, labels=pieLabels)                        #Labels will be added to legend
mplt.legend(title = "Pie Chart Values")                     #Title of legend + labels will be added
mplt.title('With Legend')
mplt.show()


    #colors
colors = ['r', 'm', 'y', 'g', '#abcdef']                    #Specific colors for the pie
mplt.pie(pieChart, colors=colors)                           #Add Colors
mplt.title('Specific')
mplt.show()