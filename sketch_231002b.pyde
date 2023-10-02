from random import randrange
def setup():
    size(500,500)
    background(0,25,255)

x = 100
y = 100
direction = [0,1]
def draw():
    global direction
    global x 
    global y
    
    noStroke()
    bw = width * 0.3
    bh = height * 0.3
    left = (width - bw) / 2
    top = (height - bh) / 2
    
    if mouseX > left and mouseX < left + bw and mouseY > bh and mouseY < top + bh:
        fill(255,0,0)
    else:
        fill(255,255,0)
    rect(left,top,bw,bh)    
    fill(random(0,255),random(0,255),random(0,255))
    circle(x,y,40)
    x += direction[0]
    y += direction[1]
    if x > width or x <0 or y>height or y < 0:
        direction[0] = random(-1,1)
        direction[1] = random(-1,1)
    if x > width+20 or x <-20 or y>height+20 or y <-20:
         x = 250
         y = 250
    
