"""Classify a remotely sensed image"""
import gdalnumeric

# Input file name (thermal image)  
src = "thermal.tif"

# Output file name
tgt = "classified.jpg"

# Load the image into numpy using gdal
srcArr = gdalnumeric.LoadFile(src)

# Split the histogram into 20 bins as our classes
classes = gdalnumeric.numpy.histogram(srcArr, bins=20)[1]

# Color look-up table (LUT) - must be len(classes)+1.
# Specified as R,G,B tuples 
lut = [[255,0,0],[191,48,48],[166,0,0],[255,64,64],
[255,115,115],[255,116,0],[191,113,48],[255,178,115],
[0,153,153],[29,115,115],[0,99,99],[166,75,0],
[0,204,0],[51,204,204],[255,150,64],[92,204,204],[38,153,38],[0,133,0],
[57,230,57],[103,230,103],[184,138,0]]

# Starting value for classification
start = 1

# Set up the RGB color JPEG output image
rgb = gdalnumeric.numpy.zeros((3, srcArr.shape[0], srcArr.shape[1],), gdalnumeric.numpy.float32)
       
# Process all classes and assign colors
for i in range(len(classes)):
    mask = gdalnumeric.numpy.logical_and(start <= srcArr, srcArr <= classes[i])
    for j in range(len(lut[i])):
        rgb[j] = gdalnumeric.numpy.choose(mask, (rgb[j], lut[i][j]))
    start = classes[i]+1 

# Save the image    
gdalnumeric.SaveArray(rgb.astype(gdalnumeric.numpy.uint8), tgt, format="JPEG")

