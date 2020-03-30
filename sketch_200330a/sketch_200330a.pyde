pos_x = 150
pos_y = 0

sagHallo = u'Hallo'

def setup():
    size(852, 480)
    backgroundImg = loadImage("background.png")
    background(backgroundImg)
    
    figurImg = loadImage("figur.png")
    global figurImg
    font = createFont("Verdana-Bold", 64)
    textFont(font)
    
    
def keyPressed():
        
    if key == "a":
        print("a")
    elif key == "w":
        print("w")
    elif key == "d":
        print("d")
    elif key == "s":
        print("s")


    
def draw():
    backgroundImg = loadImage("background.png")
    image(figurImg, pos_x, pos_y)
    text(sagHallo, 350, 90)
