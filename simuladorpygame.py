from pygame import *
import sys
import math

init()
screen = display.set_mode((1280, 720))
fondo =  transform.scale(image.load("simulador_page-0001.jpg"), (1280,720))

def coord(ang, vinicial):
    ang1 = math.radians(ang)
    x1 = 0 
    ycoord = []
    xcoord = []

    while x1 < 1000:
        y1 = (x1*math.tan(ang1))-((9.8*x1*x1))/(2*(vinicial*vinicial)*(math.cos(ang1)*math.cos(ang1)))
        x1 = x1 + 50
        ycoord.append(y1)
        xcoord.append(x1)

    return xcoord, ycoord


def animr(xcoordr, ycoordr, color):
    puntos = 0
    while puntos < len(xcoordr):
        draw.rect(screen, (0, 255, 0), (xcoordr[puntos], 300-ycoordr[puntos], 10, 10), 3)
        time.delay(300)
        display.update()
        puntos += 1
        


while True:
    screen.fill((255, 255, 255))
    screen.blit(fondo, (0,0))
    for e in event.get():
        if e.type == QUIT: sys.exit()
    draw.rect(screen, (0,0,255), (399,-120, 312, 100), 3) 
    draw.circle(screen, (0,0,255), (399, 400), 10, 1)
    display.flip()