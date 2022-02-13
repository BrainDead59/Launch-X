#Ejercicio 1)
planet = {
    'name':'Mars',
    'moons':2
}
print("Planet:" + str(planet.get('name')) + "\nMoons:" + str(planet.get('moons')))

planet['circunferencia(km)']={
    'polar': 6752,
    'equatorial': 6792
}

print("Planeta:"+ planet['name'] + "\nCircunferencia polar:"+str(planet['circunferencia(km)']['polar']))

#Ejercicio 2)
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

moons = planet_moons.values()
planets = len(moons)
total_moons=sum(moons)
total_moons = total_moons/planets
print("Lunas promedio:"+str(total_moons))
