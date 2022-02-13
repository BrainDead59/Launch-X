#Primer ejercicio
def informe(*args):
    return 'El promedio oxígeno es:' + str(promedio(*args))

def imprimir_informe():
    print(informe(19,10,123))

def promedio(*args):
    return sum(args)/len(args)

imprimir_informe()

#Segundo ejercicio
def informe_preciso(destino, *minutes,**fuel_reservoirs):
    reporte=f'Destino:{destino}\nTiempo de viaje:{sum(minutes)}\nGasolina:{sum(fuel_reservoirs.values())}\n'
    for nombre, litros in fuel_reservoirs.items():
        reporte+= f'Tanque {nombre}: {litros} litros\n'
    return reporte  

print(informe_preciso("Moon", 8, 11, 55, main=300000, external=200000))
