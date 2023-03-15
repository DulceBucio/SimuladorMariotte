from pygame import *
import sys
import math

init()
screen = display.set_mode((1280, 720))
fondo =  transform.scale(image.load("simulador_page-0001.jpg"), (1280,720))

while True:
    screen.fill((255, 255, 255))
    screen.blit(fondo, (0,0))

    for e in event.get():
        if e.type == QUIT: sys.exit()
    
    display.flip()