# -*- coding: utf-8 -*-
"""

#created by Liz Goldstein 7/24/19
#combine two photos, one with greenscreen
#Import necessary image processing module from PIL package

"""

from PIL import Image 

#Function to tell if RGB values result in green or not 

  
    
#Open the image files 
image_green = Image.open("green1.jpg")
new_backg = Image.open("paris4.JPG")


#This program works with images that are square and the same size
#Feed the images through the changeImageSize function to get same size images
image_g = image_green.resize((500,500))
image_b=new_backg.resize((500,500))
#image_b.show()

#Create Output Image
raw_output=image_g
height=raw_output.height
width=raw_output.width

#load data regarding green screen so faster processing
green_smaller_load = image_g.load()
backg_smaller_load = image_b.load()


#iterate through each pixel and get the r, g, b values
for i in range(width):
    for j in range(height):
        r=green_smaller_load[i,j][0] 
        g=green_smaller_load[i,j][1]
        b=green_smaller_load[i,j][2]
        #When the pixel is green (meaning if below statement is true), replace it with B's Value
        if 0<= r <255 and 105 < g <=255 and 0<= b <255:
           #fill in green pixel with pixel in same spot in background photo 
            back_color = backg_smaller_load[i,j] 
            raw_output.putpixel((i,j),back_color) #Set the output pixel 


#Save the resulting image in C 
raw_output.save("parisgreen.png")
raw_output.show()
