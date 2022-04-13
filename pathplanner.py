#!/usr/bin/python3
"""
pathplanner.py
Generates a motion profile based on a spline curve defined in an
actual field layout

Dave Cohen - wezelball
"""
import matplotlib.pyplot as plt

def onclick(event):
    """ A callback for the mouse button click.
    Returns the coordinates of the mouse click and which button was clicked.
    Button1: left click
    Button2: middle click
    Button1: right click
    xdata = x-coordinate (field units of inches) of button click
    ydata = y-coordinate (field units of inches) of button click
    """
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

    # Add a point ot the scatter plot
    ax.scatter([event.xdata], [event.ydata], c='r', s=40)
    ax.arrow(event.xdata, event.ydata, 10.0, 0.0 )
    # Update the scatter point
    fig.canvas.draw() 
    
# The actual field width that is accessible by the robot
field_width = 54.0*12.0     # units of inches - 648"
field_height = 27.0*12.0    # units of inches - 324"
#image_width = 1052          # units of pixels
#image_heght = 526           # units of pixels

fig,ax = plt.subplots()

# Read in the field drawing
im = plt.imread('FE-2022_crop.png')

# The extent modifier converts the 1052 x 526 image to 648" x 324",
# with 0,0 at lower left of field
implot = ax.imshow(im, extent = (0,field_width,0,field_height))

# put a blue dot at (324, 162), which is center of field
#plt.scatter([324], [162])
# put a red dot, size 40, at center of field
ax.scatter([324], [162], c='r', s=40)

# Connection id returns an integer and creates a callback to the onclick
# event
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Show the plot
plt.show()
