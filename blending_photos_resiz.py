# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 20:42:59 2019

@author: Owner
"""

from PIL import Image

# Take two images for blending them together   
image1 = Image.open("jackie.jpg")
image2 = Image.open("loveis2.jpg")

# Make the images of uniform size
image1 = image1.resize((400, 400))
image2=image2.resize((400, 400))

# Make sure images got an alpha channel
image1 = image1.convert("RGBA")
image2 = image2.convert("RGBA")


# alpha-blend the images with varying values of alpha
alphaBlended1 = Image.blend(image1, image2, alpha=.3)
alphaBlended2 = Image.blend(image1, image2, alpha=.8)

# Display the alpha-blended images
alphaBlended1.show()
alphaBlended2.show()
#save image
alphaBlended2.save("jackie_nose1.png")
alphaBlended2.save("jackie_nose2.png")


