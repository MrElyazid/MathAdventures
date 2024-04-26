# system constants


l1 = 100.0
l2 = 100.0
m1 = 10.0
m2 = 10.0
theta1 = PI/4
theta2 = PI/6
g = 9.81

v1 = 0.0 # angular velocity for first pendulum
v2 = 0.0 # angular velocity for the second pendulum


dt = 0.05

def setup():
    size(600, 400)
    background(255)
    frameRate(80)
    
    
def draw():
    global theta1, theta2, v1, v2
    
    # acceleration for the first angle theta1 
    term1 = -g*(2*m1+m2)*sin(theta1) - m2*g*sin(theta1-2*theta2)
    term2 = -2*sin(theta1-theta2)*m2*((v2**2)*l2+v1*l1*cos(theta1-theta2))
    den1 = l1*(2*m1+m2-m2*cos(2*theta1-2*theta2))
    a1 = (term1 + term2)/den1
    
    # acceleration for the second angke theta2
    term3 = 2*sin(theta1-theta2)*((v1**2)*l1*(m1+m2))
    term4 = g*(m1+m2)*cos(theta1)
    term5 = (v2**2)*l2*m2*(cos(theta1-theta2))
    den2 = l2*(2*(m1+m2)-m2*cos(2*theta1-2*theta2))
    a2 = (term3 + term4 + term5)/den2
    
    # getting the velocities using a (first order derivative approx ?), then we will get the new positions
    v1 = v1 + a1*dt # basically v(t+dt) = v(t) + a1*dt , the definition of velocity
    v2 = v2 + a2*dt
    
    # now getting the angles from the angluar velocities
    theta1 = theta1 + v1*dt
    theta2 = theta2 + v2*dt
    
    
    # de coordonnées polaires aux coordonnées cartesiennes 
    x1 = l1*sin(theta1)
    y1 = l1*cos(theta1)
    x2 = x1 + l2*sin(theta2)
    y2 = y1 + l2*cos(theta2)
    
    
    background(255)
    translate(width/2, height/4)
    stroke(0)
    strokeWeight(2)
    
    line(0, 0, x1, y1)
    line(x1, y1, x2, y2)
    
    fill(0)
    ellipse(x1, y1, 10, 10)
    ellipse(x2, y2, 10, 10)
                         
    
