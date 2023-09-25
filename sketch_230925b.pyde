
circle1 = 0
circle2 = 0
circle3 = 0
circle3y = 0
circle4 = 0
circle4y = 0
rad = 2
iteration = 0
def setup():
    size(500,500)
    color(HSB)
    global circle1 
    circle1 = width/2
    global circle2
    circle2 = width/2
    global circle3 
    circle3 = width/2
    global circle3y 
    circle3y = width/2
    global circle4
    circle4 = width/2
    global circle4y
    circle4y = width/2
    background(1,1,255)
    noStroke()
def draw():
    global circle1
    global circle2
    global circle3
    global circle3y
    global circle4
    global circle4y
    global rad
    global iteration
    
    x = random(1,255)
    y = random(1,255)
    z = random(1,255)
    
    rad = random(1,150)
    iteration +=1
    fill(x,y,z)
    if(circle1 >=40):
        circle1 -= 1
    circle(circle1,circle1, rad)
    if(circle2 <= 460):
        circle2 += 1
    circle(circle2,circle2, rad)
    if(circle3 <= 460):
        circle3 += 1
        circle3y -= 1
    circle(circle3,circle3y, rad)
    if(circle4 >= 40):
        circle4 -= 1
        circle4y += 1
    circle(circle4,circle4y, rad)
    
    if(iteration >300):
        background(1,1,255)
        circle1 = width/2
        circle2 = width/2
        circle3 = width/2
        circle3y = width/2
        circle4 = width/2
        circle4y = width/2
        rad = 1
        iteration = 0
    
    
