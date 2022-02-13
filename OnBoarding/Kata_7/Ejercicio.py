#Ejercicio 1)
new_planet=''
planets=[]
while new_planet!='done':
    if new_planet!='':
        planets.append(new_planet)
    new_planet=input('Inserta un nuevo planeta:')

#Ejercicio 2)
for planet in planets:
    print(planet)