from math import sqrt

# range of x-values

xmin = -2
xmax = 2

# range of y-values

ymin = -2
ymax = 2

rangex = xmax - xmin
rangey = ymax - ymin


def cAdd(a,b):
    return [a[0]+b[0], a[1]+b[1]]

def cMul(a,b):
    return [a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]]

def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)

def mandelbrot(z,num):
    count = 0
    z1 = z
    while count <= num:
        if magnitude(z1) > 2.0:
            return count
        z1 = cAdd(cMul(z1,z1),z)
        count += 1
        
    return num


def setup():
    global xscl, yscl
    size(600,600)
    colorMode(HSB)
    noStroke()
    xscl = float(rangex)/width
    yscl = float(rangey)/height
    
    
def draw():
    
    for x in range(width):
        for y in range(height):
            z = [(xmin + x*xscl), (ymin + y*yscl)]
            col = mandelbrot(z,100)
            
            if col == 100:
                fill(0)
            else:
                fill(3*col, 255, 255)
            rect(x,y,1,1)
