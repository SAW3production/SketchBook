def setup():
    size(500,500)
    background(255,0,0)
    
    
def draw():
    background(255,0,0)
    noStroke()
    fill(255,0,0)

    fill(255,255,0)
    circle(250,250,400)
    fill(2,225,255)
    triangle(250,10,10,420,490,420)
    fill(255,255,225)
    if mousePressed:
        fill(255,255,225)
        ellipse(250,235,250,100)
        fill(0,0,0)
        ellipse(mouseX,mouseY,40,-90)
    else:
        fill(255,255,225)
        ellipse(250,235,250,100)
        fill(0,0,0)
        ellipse(250,235,40,-90)
        

    
