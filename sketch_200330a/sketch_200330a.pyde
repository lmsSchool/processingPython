pos_x = 150    #Startposition für Figur
pos_y = 0      #Startposition für Figur 
<<<<<<< HEAD
STEP = 3

radius_x = 50  # Bildbreite/2
radius_y = 85  # Bildhöhe/2
=======

radius_x = 50  # Bildbreite/2
radius_y = 85  # Bildhöhe/2
STEP = 5       # Geschwindigkeit
>>>>>>> 0b2f6971e06c2d2edff87ebc47f438d8bf50801b

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
<<<<<<< HEAD
    
    background(backgroundImg)
    text(sagHallo, 350, 90)
    
    image(figurImg, pos_x, pos_y)
    
    
    
    
    #Auf Tasten achten 
    #Bewegung steuern
    if key == "w":
        pos_y -= STEP 
        print("Taste w wurde gedrueckt")
    elif key == "s":
        pos_y += STEP
        print("Taste s wurde gedrueckt")
    elif key == "a":
        pos_x -= STEP
        print("Taste a wurde gedrueckt")
    elif key == "d":
        pos_x += STEP
        print("Taste d wurde gedrueckt")
    

    
    
=======
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
>>>>>>> 0b2f6971e06c2d2edff87ebc47f438d8bf50801b
