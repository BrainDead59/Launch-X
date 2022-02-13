#Primer ejercicio 1)
planetas = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print('Cantidad de planetas:' + str(len(planetas)))
planetas.append('Pluton')
print('Cantidad de planetas:' + str(len(planetas)))
print('Ultimo elemento: %s' %(planetas[(len(planetas)-1)]))

#Segundo ejercicio 2)
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
planeta_indice=input('Inserta el nombre de un planeta: ')
indice = planets.index(planeta_indice)
planetas_cercanos = planets[0:indice]
print('Planetas cercanos: ' + str(planetas_cercanos))
planetas_lejanos =  planets[indice+1:]
print('Planetas lejanos: ' + str(planetas_lejanos))