#!/usr/bin/python3

import matplotlib.pyplot as plt

field_width = 54.0*12.0     # units of inches - 648"
field_height = 27.0*12.0    # units of inches - 324"
#image_width = 1052          # units of pixels
#image_heght = 526           # units of pixels

# Read in the field drawing and plot
im = plt.imread('FE-2022_crop.png')

# The extent modifier converts the 1052 x 526 image to 648" x 324",
# with 0,0 at lower left of field
implot = plt.imshow(im, extent = (0,field_width,0,field_height))

# put a blue dot at (324, 162), which is center of field
#plt.scatter([324], [162])
# put a red dot, size 40, at center of field
plt.scatter([324], [162], c='r', s=40)

# put a red dot, size 40, at 2 locations:
# plt.scatter(x=[30, 40], y=[50, 60], c='r', s=40)

plt.show()
