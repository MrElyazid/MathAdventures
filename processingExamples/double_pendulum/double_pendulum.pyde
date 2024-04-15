def setup():
    global r1, r2, m1, m2, a1, a2, a1_v, a2_v, g
    size(640, 360)
    pixelDensity(displayDensity())
    r1 = 125
    r2 = 125
    m1 = 10
    m2 = 10
    a1 = PI / 2
    a2 = PI / 2
    a1_v = 0
    a2_v = 0
    g = 1

def draw():
    global a1, a2, a1_v, a2_v
    background(255)
    translate(width / 2, height / 4)
    
    # Equations of motion
    num1 = -g * (2 * m1 + m2) * sin(a1)
    num2 = -m2 * g * sin(a1 - 2 * a2)
    num3 = -2 * sin(a1 - a2) * m2
    num4 = a2_v * a2_v * r2 + a1_v * a1_v * r1 * cos(a1 - a2)
    den = r1 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
    a1_a = (num1 + num2 + num3 * num4) / den

    num1 = 2 * sin(a1 - a2)
    num2 = (a1_v * a1_v * r1 * (m1 + m2))
    num3 = g * (m1 + m2) * cos(a1)
    num4 = a2_v * a2_v * r2 * m2 * cos(a1 - a2)
    den = r2 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
    a2_a = (num1 * (num2 + num3 + num4)) / den

    
    a1_v += a1_a
    a2_v += a2_a

    
    a1 += a1_v
    a2 += a2_v

    # first pendulum
    x1 = r1 * sin(a1)
    y1 = r1 * cos(a1)
    fill(0)
    line(0, 0, x1, y1)
    ellipse(x1, y1, m1, m1)

    # second pendulum
    x2 = x1 + r2 * sin(a2)
    y2 = y1 + r2 * cos(a2)
    line(x1, y1, x2, y2)
    ellipse(x2, y2, m2, m2)
