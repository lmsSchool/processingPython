pos_x = 150    #Startposition für Figur
pos_y = 0      #Startposition für Figur 

radius_x = 50  # Bildbreite/2
radius_y = 85  # Bildhöhe/2
STEP = 5       # Geschwindigkeit

sagHallo = u'Hallo '

def setup():
    size(852, 480)
    backgroundImg = loadImage("background.png")
    background(backgroundImg)
    
    figurImg = loadImage("figur.png")
    global figurImg
    font = createFont("Verdana-Bold", 64)
    textFont(font)
    
    
def draw():
    global pos_x, pos_y
    backgroundImg = loadImage("background.png")
    background(backgroundImg)
    text(sagHallo, 350, 90)
    image(figurImg, pos_x, pos_y)
    
    #Bewegung steuern        
    if key == "a":
        pos_x -= STEP
        print("a")
    elif key == "w":
        pos_y -= STEP
        print("w")
    elif key == "d":
        pos_x += STEP
        print("d")
    elif key == "s":
        pos_y += STEP
        print("s")
    if pos_x > width + radius_x:
        pos_x = -radius_x
    elif pos_x < -2*radius_x:
        pos_x = width + radius_x
    if pos_y < -2*radius_y:
        pos_y = height
    elif pos_y > height:
        pos_y = -radius_y
