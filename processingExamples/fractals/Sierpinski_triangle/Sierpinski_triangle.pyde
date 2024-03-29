def sierpinski(sz, level):
    if level == 0:
        fill(0)
        triangle(0,0,sz,0,sz/2.0, -sz*sqrt(3)/2.0)
    else:
        for i in range(3):
            sierpinski(sz/2.0, level-1)
            translate(sz/2.0, -sz*sqrt(3)/2.0)
            rotate(radians(120))
        



def setup():
    size(600,600)
    
    
def draw():
    background(255)
    translate(100,450)
    level = int(map(mouseX, 0, width, 0, 10))
    sierpinski(400, level)
