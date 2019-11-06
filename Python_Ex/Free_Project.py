#Free Project 11-1
#%%
from PIL import Image, ImageDraw

def transformimage(text, bgcolor): 
    img = Image.new('RGB', (100, 40), color = bgcolor)
    d = ImageDraw.Draw(img)
    d.text ((10,10), text, fill = (255,255,255))
    return img

transformimage("Hello World", "black")

#%%
from PIL import Image, ImageDraw

def transformimage(text, bgcolor): 
    img = Image.new('RGB', (100, 40), color = bgcolor)
    d = ImageDraw.Draw(img)
    d.text ((10,10), text, fill = (255,255,255))
    return img
#The output for this is a black square with white text.
#I could have changed the colors to make them more interesting but decided against that.
transformimage("Hello World", "black")

#I attempted to make the image rotate. however this failed without an error
img_rot_90 = img.rotate(90)
