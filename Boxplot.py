# Matplotlib Basics - written by V I E R U S
# June 8, 2022
# If not already install matplotlib with 'pip install matplotlib' and 'pip install numpy' with cmd
# This program goes into the basics of matplotlib Box Plot/Whisker Plot

#Create a BP, Horizontal, Width, label, color box/outline/lines/cap/outliner, outliner, connect outliner, Multiple values

#-------------------------------------------------------------------------
#Imports
from matplotlib import *
import matplotlib.pyplot as mplt
import numpy as np


#Box Plot-----------------------------------------------------------------------------------------
#Box Plots------------------------------------------
    #num1
xboxP = np.array([-2,0,1,4,6,7])

    #num2
xboxP2 = np.array([-1,1,3,5,8,9,10,30])

    #num3
xboxP3 = np.array([-1,1,3,5,8,9,10])


#Box Plots END--------------------------------------
    #Create a box plot - num1
mplt.boxplot(xboxP)
mplt.title('Created a Box Plot')                    #-2 Min,7 Max horizontal lines, red line medium(Q2), rectangle based on quantiles (Q1-Q3)
mplt.show()


    #Horizontal - num1
mplt.boxplot(xboxP, vert=False)
mplt.title('Horizontal Box Plot')
mplt.show()


    #Width - num1
mplt.boxplot(xboxP, widths=0.5)                     #Width default is around .15
mplt.title('Change Width of Box Plot')
mplt.show()


    #Label Box Plot - num1
mplt.boxplot(xboxP, labels=["BP one"])
mplt.title('Label Box Plot')
mplt.show()


    #Color box in box plot - num1
mplt.boxplot(xboxP, patch_artist=True)              #Default is false
mplt.title('Color Box in Box Plot')
mplt.show()


    #Change outline color - num1
mplt.boxplot(xboxP, boxprops=dict(color='m'))
mplt.title('Change Color outline')
mplt.show()


    #Change lines color - num1
mplt.boxplot(xboxP, whiskerprops=dict(color='g'))
mplt.title('Change Color line')
mplt.show()

    #Change cap(Min/Max) color - num1
mplt.boxplot(xboxP, capprops=dict(color='b'))
mplt.title('Change Color Cap')
mplt.show()

    
    #Outliner - num2
mplt.boxplot(xboxP2, labels=['BP two'])
mplt.title('outliner of Box Plot')
mplt.show()
    
    
    #Connect outliner to boxplot - num2
mplt.boxplot(xboxP2, whis=3.5 )
mplt.title('Connecting Outliner to Box Plot')
mplt.show()


    #Change color of outliner - num2
mplt.boxplot(xboxP2, sym="g*" )
mplt.title('Color Outliner Box Plot')
mplt.show()


    #Multiple Values - num1 num3
mplt.boxplot([xboxP, xboxP3], labels=['BP 1', 'BP 3'])
mplt.title('Multiple Values')
mplt.show()