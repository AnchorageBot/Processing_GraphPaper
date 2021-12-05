# This script will plot the function f(x**2)

# Source code/software
    # Math Adventures with Python by Peter Farrell, Chapter 4+
    # Made with Processing 3.5.4 using Python Mode in Dec 2021
      # https://py.processing.org

#range of x-values
xmin = -10
xmax = 10
#range of y-values 
ymin = -10
ymax = 10
#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin
 
def setup():
    global xscl, yscl 
    size(600,600)
    xscl = width / rangex
    yscl = -height / rangey

def draw():
    global xscl, yscl
    background(255)
    translate(width/2,height/2)
    grid(xscl,yscl) #draw the grid
    graphFunction()

def f(x):
    return x**2

def graphFunction():
    x = xmin
    while x <= xmax:
        stroke(0)
        line(x*xscl, f(x)*yscl, (x+0.1)*xscl, f(x+0.1)*yscl)
        x += 0.1
          
def grid(xscl,yscl):
    #Draws a grid for graphing
    #cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin,xmax+1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
    for i in range(ymin,ymax+1):
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
    # black axes    
    stroke(0)
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)
