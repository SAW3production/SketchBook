def setup():
    global cx, cy
    size(500, 500)
    colorMode(HSB)
    cx = width / 2
    cy = height /2
    
cx = 0
cy = 0
r = 150
gr = 50
    
def draw():    
    global cx, cy
    global r,gr
    num = 5
    theta = TWO_PI / num
    
    background(0)
    noStroke()
    strokeWeight(2)
    
    #out
    for i in range(num):
        angle = theta * i
        
        
        x = cx + sin(angle) * gr
        y = cy + cos(angle) * gr
        stroke(200, 255, 255)
        
        
        fill(200, 255, 300)
        circle(x, y, r)
    
            
    #lines
    for i in range(num):
        angle = theta * i
        c = (i / float(num)) * 255
        print(c)
        
        
        x = cx + sin(angle) * 120
        y = cy + cos(angle) * 120
        stroke(200,255,150)
        line(cx,cy,x,y)
    #in
    for i in range(num):
        angle = theta * i
        
        
        x = cx + sin(angle) * 20
        y = cy + cos(angle) * 20
        stroke(200, 255, 255)
        
        
        fill(200, random(180,255), 300)
        circle(x, y, random(70,100))
    
    noStroke()
    fill(1)
    circle(cx,cy,20)
        
  


    
