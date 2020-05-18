pos_x = 150    #Startposition für Figur
pos_y = 0      #Startposition für Figur 
STEP = 3

radius_x = 50  # Bildbreite/2
radius_y = 85  # Bildhöhe/2

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
    

    
    
