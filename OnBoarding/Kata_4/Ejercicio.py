#Ejercicio 1)
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several 
interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 
4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate 
effects on Earth. The highest daylight"""

#Dividir el texto
texto = text.split('.')

#Crear las palabras clave
palabras_clave=['average','temperature','distance']

#Recorre el texto en búsqueda de datos
for datos in texto:
    for palabra_clave in palabras_clave:
        if palabra_clave in datos:
            datos.replace('\n',',')
            print(datos)


#Cambiar C a Celsius
for datos in texto:
    for palabra_clave in palabras_clave:
        if palabra_clave in datos:
            datos.replace('\n',',')
            print(datos.replace('C','Celsius'))

#Ejercicio 2)
print("----Segundo ejercicio----")
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

#Crear titulo
titulo = f'Datos sobre la gravedad de: {name} \n'
plantilla = f'name = {name}\ngravity = {gravity*1000} [m/s^2] \nplanet = {planet} '

#Unión
datosCuerpoCeleste=titulo+plantilla
print(datosCuerpoCeleste)

planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

#Nueva plantilla
titulo = f'Datos sobre la gravedad de: {nombre} \n-----------------------------\n'
plantillaM='name = {}\ngravity = {} [m/s^2] \nplanet = {}'.format(nombre,gravedad*1000,planeta)
print(titulo + plantillaM)