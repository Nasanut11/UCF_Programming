class Bear(object):
    c=color(0, 255, 100)
    
def draw():
    background(250, 100, 100)
    frameRate(5)
    printIn(pmousex - mousexX)
  
def setup():
    size(600, 700)
    strokeWeight(.5)


def draw():
    background(250, 100, 100)
    line(mouseX, mouseY, pmouseX, pmouseY)
