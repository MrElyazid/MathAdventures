
r1 = 80
r2 = 7
r3 = 7
t = 0


sineList = []
cosineList = []

def setup():
    size(800,800)
    
    
    
def draw():
    global t, sineList,cosineList
    background(200)
    
    translate(width/4, height/4)
    noFill() # no color for the big circle
    stroke(52, 125, 235) # black outline
    ellipse(0,0,2*r1,2*r1)
    
    fill(255,0,0)
    

    y = r1*sin(-t) # the minus sign here so the dot moves in anti-clockwise direction
    x = r1*cos(t)
    
    sineList = [y] + sineList[:249]
    cosineList = [x] + cosineList[:249]
    
    ellipse(x,y,r2,r2)
    
    stroke(0, 255, 0) # green for the line
    line(x,y,200,y)
    line(x,y,x,200)
    fill(0,255,0)
    ellipse(200,y,10,10)
    ellipse(x,200,10,10)
    
    for i in range(len(sineList)):
        ellipse(200+i, sineList[i], 3,3)
        ellipse(cosineList[i], 200+i, 3,3)
    
    t+=0.05
    

    
