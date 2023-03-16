from pygame import *
import sys
import math

init()
screen = display.set_mode((1280, 720))
fondo =  transform.scale(image.load("fondo1.jpg"), (1280,720))

def coord(altura, angulo):
        alturan = 720 - altura - 10
        theta = math.pi / 4   # Ángulo de lanzamiento (en radianes)
        v0 = 20.0   # Velocidad inicial
        g = 9.81   # Aceleración debido a la gravedad

        # Calcular el tiempo en que se alcanza la altura máxima
        t_max = v0 * math.sin(theta) / g

        # Calcular el desplazamiento horizontal total
        d_total = v0 * math.cos(theta) * t_max * 2

        # Calcular los puntos a partir de la mitad del tiro parabólico
        puntos_x = []
        puntos_y = []
        for x in range(int(d_total/2), int(d_total)+1):
            t = (x / (v0 * math.cos(theta)))
            y = alturan + (v0 * math.sin(theta) * t) - (0.5 * g * t**2)
            puntos_x.append(x)
            puntos_y.append(y)

        return(puntos_x, puntos_y)


def listarecorrida(puntos_x):
    puntos_n = []
    for i in range (len((puntos_x))):
          puntonuevo = puntos_x[i] + 970
          puntos_n.append(puntonuevo)
    return puntos_n

def anim(xcoord, ycoord):
    puntos = 0
    color = (0, 0, 255)
    while puntos < len(xcoord):
        draw.circle(screen, (0,0,255), (xcoord[puntos], 720 - ycoord[puntos]), 10, 0)
        time.delay(300)
        display.update()
        puntos += 1
        
def calculos(altura):
    velocidadsalida = math.sqrt(2*9.81*altura)
    return velocidadsalida



while True:
    screen.fill((255, 255, 255))
    screen.blit(fondo, (0,0))
    for e in event.get():
        if e.type == QUIT: sys.exit()
    draw.rect(screen, (0,0,255), (399,-120, 312, 100), 3) 
    #draw.circle(screen, (0,0,255), (980, 380), 10, 0)
    #draw.circle(screen, (0,0,255), (980, 480), 10, 0)
    #draw.circle(screen, (0,0,255), (980, 580), 10, 0)
    x1, y1 = coord(380, 75)
    x11 = listarecorrida(x1)
    anim(x11, y1)
    x2, y2 = coord(480, 60)
    x22 = listarecorrida(x1)
    anim(x22, y2)
    x3, y3 = coord(580, 45)
    x33 = listarecorrida(x1)
    anim(x33, y3)
    display.flip()