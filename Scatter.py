# Matplotlib Basics - written by V I E R U S
# June 8, 2022
# If not already install matplotlib with 'pip install matplotlib' and 'pip install numpy' with cmd
# This program goes into the basics of matplotlib Scatter Plot

# Create scatter plot, marker size, transparent size, random colors/sizes markers

#----------------------------------------------------------------------------------------------
#Imports
from matplotlib import *
import matplotlib.pyplot as mplt
import numpy as np


#Scatter-------------------------------------------------------------------------------------------
#Scatter plot----------------------------------------
    #Num1
xpoint = np.array([1,2,4,6,8,10,12])                                #X points
ypoint = np.array([0,65,2,57,13,45,50])                             #Y points

    #Num2 is in code

#Scatter plot END------------------------------------
    #Create scatter plot - num1
mplt.scatter(xpoint, ypoint)                                        #Add points to scatter plot 
mplt.title("Create Scatter Plot")                     
mplt.show()                                                         #Creates GUI plot


    #Sizes markers - num1
sizes = np.array([20,50,100,200,75,60,90])                          #Make each marker a different size
mplt.scatter(xpoint, ypoint, s=sizes)                               #s=sizes will make each marker the size you decided above
mplt.title("Size Marker Plot") 
mplt.show() 


    #Transparent sizes - num1
sizes = np.array([20,50,100,200,75,60,90])
mplt.scatter(xpoint, ypoint, s=sizes, alpha=0.5)                    #alpha makes your markers transparent (Default is 1 for solid color)
mplt.title("Transparent Marker Plot") 
mplt.show() 


    #Random colors and sizes - num2
xpoint2 = np.random.randint(100, size=(100))
ypoint2 = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))                         #Random colors based off color bar shown on the side when show()
sizes = 10 * np.random.randint(100, size=(100))                     #Random sizes, based off of 1-100
mplt.scatter(xpoint2, ypoint2, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')          #Cmap >
mplt.colorbar()                                                     #Colorbar, shown on right side
mplt.title("Random Colors/Sizes Plot") 
mplt.show()