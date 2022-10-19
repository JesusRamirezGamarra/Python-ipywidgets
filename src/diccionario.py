planet = {
    'name': 'Earth',
    'moons': 1
}
print(planet)
# Lectura de valores de diccionario
print(planet.get('name'))
print(planet.get('moons'))
print(planet['name'])
print(planet['moons'])

#wibble = planet.get('wibble') # Returns None
#wibble = planet['wibble'] # Throws KeyError

# Modificación de valores de diccionario
planet.update({'name': 'Makemake'})     # name is now set to Makemake
planet['name'] = 'Makemake'             # name is now set to Makemake



# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79

# Adición y eliminación de claves

planet['orbital period'] = 4333
# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }

planet.pop('orbital period')
# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }

# Tipos de data complejos
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }


print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')
print(f"""{planet.get("name")} polar diameter: {planet.get('diameter (km)').get('polar')}""")
# Output: Jupiter polar diameter: 133709


# Programación dinámica con diccionarios
# Recuperación de todas las claves y valores

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

# Output:
# october: 3.5cm
# november: 4.2cm
# december: 2.1cm

# Determinación de la existencia de una clave en un diccionario
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1
print(rainfall['december'])
# Because december exists, the value will be 3.1


# Recuperación de todos los valores
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter')
# Output:
# There was 10.8cm in the last quarter