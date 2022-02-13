#Primera parte
velocidad_asteroide=49
if velocidad_asteroide>=49:
    print('¡Peligro inminente!')
else:
    print('Estamos a salvo :D')

velocidad_asteroide=19

if velocidad_asteroide>20:
    print('Cuidado, es la luz del asteroide')
elif velocidad_asteroide>=19:
    print('Cuidado, es la luz del asteroide')
else:
    print('Estamos a salvo :D')

#Segunda parte

tamaño_asteroide=25
velocidad_asteroide=19

if tamaño_asteroide<25 and velocidad_asteroide<25:
    print('No hay peligro')
elif tamaño_asteroide>=25 and velocidad_asteroide<25:
    print('Daño considerable de impacto, no advertencia')
elif tamaño_asteroide<25 and velocidad_asteroide>=25:
    print('No impacto, solo advertencia')
else:
    if tamaño_asteroide>=25 and velocidad_asteroide >=25:
        print('Peligro maximo')
