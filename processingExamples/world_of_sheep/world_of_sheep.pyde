from random import choice



WHITE = color(255)
BROWN = color(102,51,0)
RED = color(255,0,0)
GREEN = color(0,102,0)
YELLOW = color(255,255,0)
PURPLE = color(102,0,204)
colorList = [YELLOW, RED, WHITE, BROWN, PURPLE]



class Sheep:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.sz = 10
        self.energy = 20
        self.colour = colour
        
        
    def update(self):
        fill(self.colour)
        ellipse(self.x, self.y, self.sz, self.sz)
        
        self.energy -= 1
        
        if (self.energy < 0 ):
            sheepList.remove(self)
        
        
        # sheep can walk randomly
        move = 10
        self.x += random(-move, move)
        self.y += random(-move, move)
        fill(255)
        
        # teleport the sheep back if it goes outside the field
        
        if self.x > width:
            self.x %= width
        if self.y > height:
            self.y %= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
        
        # sheep reproduces
        if self.energy > 50:
            self.energy -= 30
            sheepList.append(Sheep(self.x, self.y, self.colour))
        
        gx = int(self.x / patchSize)
        gy = int(self.y / patchSize)
        
        grass = grassList[rows_of_grass*gx + gy]
        if not grass.eaten:
            self.energy += grass.energy
            grass.eaten = True
        
        
class Grass:
    def __init__(self, x, y, sz):
        self.x = x
        self.y = y
        self.sz = sz
        self.eaten = False
        self.energy = 5        
        
    def update(self):
        
        if self.eaten:
            fill(BROWN)
        else:
            fill(GREEN)
            
        rect(self.x, self.y, self.sz, self.sz)
        
        
grassList = []    
sheepList = []
patchSize = 10


def setup():
    global rows_of_grass
    global patchSize
    size(600,600)
    rows_of_grass = height/patchSize
    noStroke()
    
    for x in range(0, width, patchSize):
        for y in range(0, height, patchSize):
            grassList.append(Grass(x,y,patchSize))

    
    for i in range(100):
        sheepList.append(Sheep(random(width), random(height), choice(colorList)))
        
    
    
    
def draw():
    background(255)
    for grass in grassList:
        grass.update()
        
    for sheep in sheepList:
        sheep.update()
        
    
