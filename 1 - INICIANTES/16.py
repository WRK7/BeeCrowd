x1, y1 = input().split()
x2, y2 = input().split()
import math
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
Distancia = (x2-x1)**2 + (y2 - y1)**2
Distancia = math.sqrt(Distancia)
print (f'{Distancia:.4f}')