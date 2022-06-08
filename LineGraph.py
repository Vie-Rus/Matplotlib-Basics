# Matplotlib Basics - written by V I E R U S
# June 7, 2022
# If not already install matplotlib with 'pip install matplotlib' and 'pip install numpy' with cmd
# This program goes into the basics of matplotlib Line Graph

# Create Line plot, without lines, multiple points/lines, tick marks, marker pattern, marker/line width, 
  # color Marker/Lines, format shorthand, create labels, change fonts, position of labels, add grid, format grid, 
  # subplot, legend, resize graph, save graph, change line format somepoint in the graph

#----------------------------------------------------------------------------------------------
#Imports
from matplotlib import *
import matplotlib.pyplot as mplt
import numpy as np


#Line Graph-------------------------------------------------------------------------------------
#Line Plots-----------------------------------------------------
   #num1
xpoint = np.array([0,6])                                                #X points
ypoint = np.array([0,50])                                               #Y points

   #num2
xpoint2 = np.array([1,6])
ypoint2 = np.array([2,20])

   #num3
xpoint3 = np.array([1,2,4,6])
ypoint3 = np.array([2,8,1,20])  

   #num4
xpoint4 = np.array([1,2,4,6])
ypoint4 = np.array([2,8,1,20])  

   #num5-6 are in subplot

   #num7
xpoint7 = np.array([1,3,5,7,9,11,13,14,15])
ypoint7 = np.array([2,8,1,20,4,6,8,9,10])
#Line Plots END-------------------------------------------------


    #Make graph - num1
mplt.plot(xpoint, ypoint)                                                 #Add points to plots
mplt.title("Create Graph")                                                #Title
mplt.show()                                                               #create GUI plot


    #Without line - num2
mplt.plot(xpoint2, ypoint2, 'o')                                          #create plot without lines but 'O'
mplt.title("Without Lines")
mplt.show()


    #Multiple Points - num3             
mplt.plot(xpoint3, ypoint3)                                               #create plot with mupltiple points
mplt.title("Multiple Points")
mplt.show()


    #Multple Lines - num4                                      
mplt.plot(xpoint4)                                                        #Create X lines
mplt.plot(ypoint4)                                                        #Create Y lines
mplt.title("Multiple Lines")
mplt.show()


    #Change tick marks on graph - num3            
mplt.plot(xpoint3, ypoint3)   
mplt.xticks([0,2,4,6,8])                                                  #Where you want your X tick marks
mplt.yticks([0,5,10,15,20])                                               #Where you want your Y tick marks
mplt.title("Tick Marks")
mplt.show()


    #Markers Pattern - num4         
mplt.plot(ypoint4, marker='*')                                            #create plot with * as points
mplt.title("Markers Pattern")
mplt.show()


    #Markers Width - num4        
mplt.plot(ypoint4, marker='o', ms=15)                                     #create plot with * as points, ms - Marker size
mplt.title("Change Marker Width")
mplt.show()


    #Line Width - num4        
mplt.plot(ypoint4, linewidth = 15.5)                                      #Changed line width
mplt.title("Change Line Width")
mplt.show()


    #Marker color - num4             
mplt.plot(ypoint4, marker='o', ms=15, mec='m', mfc= 'y' )                 #mec - marker edge/outline color, mfc - marker face color
mplt.title("Change Marker Color")                                         #Colors added can be: Red, Green, Blue, Cyan, Magenta, Yellow, Black, White, or hexadecimal #000000
mplt.show()


    #Line Color - num4            
mplt.plot(ypoint4, color='m')                                             #Changes lines color
mplt.title("Change Line Color")
mplt.show()


    #Format shorthand > 'marker\line\color'  - num4           
mplt.plot(ypoint4, '*:r')                                                 #create plot with a dotted lines( : ), marker with ( * ) as points and ( r ) for a red line
mplt.title("Format Shorthand")
mplt.show() 


    #Format Lines - num4     
#mplt.plot(ypoint4, linestyle= 'dotted')                                  #Changes lines without format: solid(-), dotted(:), dashed(--), dashdot(-.), none(or) 
#mplt.show()
    #OR > shorthand           
mplt.plot(ypoint4, ls = ':')
mplt.title("Change Line Format")
mplt.show()


    #Create labels  - num4
mplt.plot(xpoint4, ypoint4)
mplt.title("Create Labels")
mplt.xlabel("X Label")                                                    #Created X Label
mplt.ylabel("Y Label")                                                    #Created Y Label
mplt.show()


    #Change fonts of labels
font1 = {'family':'serif', 'color':'blue', 'size':10}
font2 = {'family':'serif', 'color':'red', 'size':20}
mplt.title("Change Font of Labels", fontdict= font2)
mplt.xlabel("X Label", fontdict= font1)
mplt.ylabel("Y Label", fontdict= font1)
mplt.show()


    #Change position of Labels
mplt.title("Change Position of Labels", fontdict= font2, loc='left')      #Change position by loc, Position can be Left, Right, or Center(Default)
mplt.xlabel("X Label", fontdict= font1)
mplt.ylabel("Y Label", fontdict= font1)
mplt.show()


    #Add Grid
mplt.title("Add Grid")
mplt.xlabel("X Label")
mplt.ylabel("Y Label")
mplt.grid()                                                               #Add grids to graph, add 'axis = x or y' to make lines only go in one direction
mplt.show()


    #format in graph
mplt.title("Format Grid")
mplt.xlabel("X Label")
mplt.ylabel("Y Label")
mplt.grid(color='g', ls='-.', linewidth=1.5)                              #Change Color, line Style, Line width
mplt.show()


    #Subplot - num5
  #Plot 1
xpoint5 = np.array([1,2,4,6])
ypoint5 = np.array([2,8,1,20])
mplt.subplot(1,2,1)                                                       #1 row, 2 column, first plot
mplt.plot(xpoint5, ypoint5)
mplt.title("Subplot: Title of graph 1")                                   #Each graph will need their own title/labels

  #Plot 2 - num6
xpoint6 = np.array([0,3,5,7])
ypoint6 = np.array([10,20,30,40])
mplt.subplot(1,2,2)                                                       #1 row, 2 column, second plot
mplt.plot(xpoint6, ypoint6)
mplt.title("Subplot: Title of graph 2")
mplt.suptitle("Overall Subplot Graph")                                    #Overall title you need suptitle
mplt.show()


    #Legend - num6
mplt.plot(xpoint6, ypoint6, label='Points')                               #Labels will be the in legend
mplt.legend()
mplt.title("Created Legend")
mplt.show()  


    #Resize graph - num6
xpoint6 = np.array([0,3,5,7])
ypoint6 = np.array([10,20,30,40])
mplt.figure(figsize=(5,3), dpi=100)                                       #figsize changes the size of the graph, dpi should be 300 so when it prints out it's not pixelized
mplt.plot(xpoint6, ypoint6)
mplt.title("Resize Graph")
mplt.show() 


   #Save graph - num6
mplt.plot(xpoint6, ypoint6)
mplt.savefig('My Graph 19.png', dpi=300)                                  #savefig then 'How you want the picture to be saved'
mplt.title("Save Graph")
mplt.show() 


    #Change line format somepoint in the graph - num7
mplt.plot(xpoint7[:4], ypoint7[:4], 'r')                                  #[:#] > goes until, [#:] > starts at
mplt.plot(xpoint7[3:], ypoint7[3:], 'r--')
mplt.suptitle("Change Line format")
mplt.show() 
