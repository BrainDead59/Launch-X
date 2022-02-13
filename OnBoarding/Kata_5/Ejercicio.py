#Primer ejercicio 1)
from math import ceil
dist_tierra = 149597870
dist_jupiter = 778547200
distancia = dist_jupiter - dist_tierra
distancia_millas = distancia*0.621
print(distancia)
print(ceil(distancia_millas))

#Segundo ejercicio 2)
distanciaA = int(input('Inserta la distancia 1, en kilometros: '))
distanciaB = int(input('Inserta la distancia 2, en kilometros: '))
distancia_total = abs(distanciaA - distanciaB)
print(distancia_total)
distancia_total=distancia_total*0.621
print(distancia_total)