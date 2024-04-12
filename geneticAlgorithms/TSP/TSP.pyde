
import random

cities = []
NB_CITIES = 10

class City:
    
  def __init__(self, x,y,num):
    self.x = x
    self.y = y
    self.number = num
  
  
  def display(self):
      strokeWeight(3)
      stroke(255,0,255)
      beginShape()
      for i in self.cityNums:
          vertex(cities[i].x, cities[i].y)
          
          cities[i].display()
          endShape(CLOSE)
    
    
    
    
class Route:
    def __init__(self):
        self.distance = 0
        self.cityNums = random.sample(list(range(NB_CITIES)), NB_CITIES)
        
    
def setup():
    size(600,600)
    background(0)
    for i in range(NB_CITIES):
        cities.append(City(random.randint(50,width-50), random.randint(50,height-50),i))
        
    route1 = Route()
    route1.display()
    for city in cities:
        city.display()
        
        
        
