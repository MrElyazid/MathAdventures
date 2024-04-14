import random

def setup():
    global cities, population, best, record_distance
    size(600, 600)
    cities = []
    population = []
    NB_CITIES = 40
    POP_N = 1000

    class City:
        def __init__(self, x, y, num):
            self.x = x
            self.y = y
            self.number = num
        
        def display(self):
            fill(0, 255, 255)
            ellipse(self.x, self.y, 10, 10)
            textSize(20)
            text(self.number, self.x - 10, self.y - 10)
            noFill()

    class Route:
        def __init__(self):
            self.distance = 0
            self.cityNums = random.sample(range(NB_CITIES), NB_CITIES)
            
        def display(self):
            strokeWeight(3)
            stroke(255, 0, 255)
            beginShape()
            for i in self.cityNums:
                vertex(cities[i].x, cities[i].y)
                cities[i].display()
            endShape(CLOSE)
            
        def calcLength(self):
            self.distance = 0
            for i, num in enumerate(self.cityNums):
                next_city = self.cityNums[(i + 1) % NB_CITIES]
                self.distance += dist(cities[num].x, cities[num].y, cities[next_city].x, cities[next_city].y)
            return self.distance
        
        def mutateN(self, num):
            indices = random.sample(range(NB_CITIES), num)
            child = Route()
            child.cityNums = self.cityNums[:]
            for i in range(num - 1):
                j = (i + 1) % num
                child.cityNums[indices[i]], child.cityNums[indices[j]] = child.cityNums[indices[j]], child.cityNums[indices[i]]
            return child
        
        def crossover(self, partner):
            child = Route()
            index = random.randint(1, NB_CITIES-2)
            child.cityNums = self.cityNums[:index]
            
            if random.random() < 0.5:
                child.cityNums = child.cityNums[::-1]
            
            notinslice = [x for x in partner.cityNums if x not in child.cityNums]
            
            child.cityNums += notinslice
            return child

    for i in range(NB_CITIES):
        cities.append(City(random.randint(50, width-50), random.randint(50, height-50), i))
    
    for i in range(POP_N):
        population.append(Route())
    
    best = random.choice(population)
    record_distance = best.calcLength()

def draw():
    global best, record_distance, population
    background(0)
    best.display()
    println(record_distance)
    
    population.sort(key=lambda route: route.calcLength())
    population = population[:1000]
    length1 = population[0].calcLength()
    
    if length1 < record_distance:
        record_distance = length1
        best = population[0]
    
    new_population = population[:250]  # Keep top 25% of the existing population
    
    for _ in range(750):  # Breed to refill population
        parentA, parentB = random.sample(new_population, 2)
        child = parentA.crossover(parentB)
        if random.random() < 0.1:  # Mutation chance
            child = child.mutateN(random.randint(2, 5))
        new_population.append(child)
    
    population = new_population
