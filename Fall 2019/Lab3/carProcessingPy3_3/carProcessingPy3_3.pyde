class Cat(object):
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 50, 20);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
    
myCat1 = Cat(color(random(255)), 0, 10, 1)
myCat2 = Cat(color(0, 255, 0), 0, 20, 2)
myCat3 = Cat(color(0, 255, 250), 0, 30, 3)
myCat4 = Cat(color(200, 25, 0), 0, 40, 4)
myCat5 = Cat(color(100, 155, 100), 0, 50, 5)
myCat6 = Cat(color(50, 55, 50), 0, 60, 1000)
    
def setup():
    size(500,200)

def draw(): 
  background(250, 155, 100)
  myCat1.drive()
  myCat1.display()
  myCat2.drive()
  myCat2.display()
  myCat3.drive()
  myCat3.display()
  myCat4.drive()
  myCat4.display()
  myCat5.drive()
  myCat5.display()
  myCat6.drive()
  myCat6.display()
  
