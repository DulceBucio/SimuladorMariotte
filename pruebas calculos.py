import math
import matplotlib.pyplot as plt

# Parámetros del tiro parabólico
h_max = 20.0   # Altura máxima
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
    y = h_max + (v0 * math.sin(theta) * t) - (0.5 * g * t**2)
    puntos_x.append(x)
    puntos_y.append(y)

# Graficar los puntos
plt.plot(puntos_x, puntos_y)
plt.xlabel('Desplazamiento horizontal')
plt.ylabel('Altura')
plt.title('Tiro parabólico')
plt.show()