# Matplotlib Basics - written by V I E R U S
# June 7, 2022
# If not already install matplotlib with 'pip install matplotlib' and 'pip install numpy' with cmd
# This program goes into the basics of matplotlib Bar Graph

# Create a Bar Graph(BG), horizontal BG, Height/width, Patterns, Add Colors, tick marks, Labels, and Figsize

#--------------------------------------------------------------------------------------------------
#Imports
from matplotlib import *
import matplotlib.pyplot as mplt
import numpy as np


#Bar Graph-----------------------------------------------------------------------------------------
#Bar Plots-----------------------------------------
    #num1
xbarG = np.array(["A", "B", "C"])                                 #X > what each bar is
ybarG = np.array([4,2,6])                                         #Y > How tall each bar is

#Bar Plots END-------------------------------------
   #Create bar Graph
mplt.bar(xbarG, ybarG)                                            #Add points to bar plots
mplt.show()                                                       #Creates Bar GUI


   #Horizontal bar graphs
mplt.barh(xbarG, ybarG)                                           #Add points to bar horizontal plot
mplt.show()


   #Bar Heigh, default height/weight is 0.8 
mplt.barh(xbarG, ybarG, height=1.0)                               #Height for horizontal, is the same as width but only for horizontal bar graph 
mplt.show()


    #Add pattern 
bars = mplt.bar(xbarG, ybarG)
# bars[0].set_hatch('/') 
# bars[1].set_hatch('*')
# bars[2].set_hatch('o') 
     #OR Shorthand
patterns = ['/', '*', 'o']
for bar in bars:
    bar.set_hatch(patterns.pop(0))
mplt.show()


   #To add color is the same as line graph
mplt.bar(xbarG, ybarG, color='r')                               #Colors added can be: Red, Green, Blue, Cyan, Magenta, Yellow, Black, White, or hexadecimal #000000
mplt.show()


   #Tick marks
mplt.bar(xbarG, ybarG)
mplt.yticks([2,4,6])                                            #Where you want your Y tick marks
mplt.xticks([0,1,2])                                            #Where you want your X tick marks
mplt.show()


   #Labels
mplt.bar(xbarG, ybarG)
mplt.xlabel("X Labels")                                         #Create X Labels
mplt.ylabel("Y Labels")                                         #Create Y Labels
mplt.title("Title Of Bar Graph")
mplt.show()


   #figsize is same as line graph
mplt.bar(xbarG, ybarG)
mplt.figure(figsize=(5,3))                                      #figsize changes the size of the graph
mplt.show()