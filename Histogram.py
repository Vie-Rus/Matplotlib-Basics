# Matplotlib Basics - written by V I E R U S
# June 8, 2022
# If not already install matplotlib with 'pip install matplotlib' and 'pip install numpy' with cmd
# This program goes into the basics of matplotlib Histogram

#Creates histogram, color edge/bar, outline, bins, width, two values, legend, horizontal

#----------------------------------------------------------------------------------------------
#Imports
from matplotlib import *
import matplotlib.pyplot as mplt
import numpy as np


#Histograms----------------------------------------------------------------------------------------
#hist Plot-------------------------------------
    #num1
xhistG = np.random.normal(25,10,30)                 #concentrated values, standard deviation, generaten array with x amount of values

    #num2
xhistG2 = np.array([2,4,7,9,12,15,6])                     #Manual input needs brackets

    #num3
xhistG3 = np.array([3,5,8,10,13,17,2])

#Hist Plot End---------------------------------
    #Create a histogram - num1
mplt.hist(xhistG)                                   #add values to histogram
mplt.title("Creates a Histogram")                   #Add Title
mplt.show()                                         #Creates GUI histogram


    #Edge Colors - num1
mplt.hist(xhistG, edgecolor = 'black')              #Edgecolor can change help see the different bars
mplt.title("Change edge colors")
mplt.show()


    #Color bar - num1
mplt.hist(xhistG, color = 'm', edgecolor = 'b')
mplt.title('Change Color of Bar')
mplt.show()


    #Color Outline Only - num2
mplt.hist(xhistG2, histtype='step')    #histtype does outline
mplt.title("Outline bar only")
mplt.show()


    #bin > certain amount shown - num2
mplt.hist(xhistG2, bins =3, edgecolor = 'black')
mplt.title('Shown only 3 out of 5')
mplt.show()


    #Width - num2
mplt.hist(xhistG2, bins =3, rwidth=0.5)             #Default 1
mplt.title('Change Width')
mplt.show()


    #Two values - num2 num3
mplt.hist([xhistG2, xhistG3])             #Default 1
mplt.title('Two values')
mplt.show()


    #Legend - num1 num2
mplt.hist([xhistG, xhistG2], edgecolor = 'b', label=['Value type 1', 'Value type 2'])
mplt.title('Add legend')
mplt.legend()
mplt.show()


    #Labels
mplt.xlabel('X Labels')
mplt.ylabel('Y Labels')
mplt.title('Add labels')
mplt.show()


    #Horizontal - num1
mplt.hist(xhistG, orientation='horizontal', edgecolor = 'black')
mplt.title('horizontal Graph')
mplt.show()
