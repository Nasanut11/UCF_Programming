# Even though there are multiple objects, we still only need one class. 
# No matter how many cookies we make, only one cookie cutter is needed.
class Car(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
    
myCar1 = Car(color(random(255)), 0, 100, 2)
myCar2 = Car(color(0, 255, 0), 0, 10, 1)
    
def setup():
    size(500,200)

def draw(): 
  background(255)
  myCar1.drive()
  myCar1.display()
  myCar2.drive()
  myCar2.display()
  
  # What follows is to initiate the spacebar event 
  def draw():
      spacebar(keyReleased)
  def keyReleased(spacebar):
    global value
    if value == 0:
        value = 255
    else:
        value = 0
