def rocket_parts():
    print("payload, propellant, structure")
    
rocket_parts()

output = rocket_parts()
print ( output is None )


def rocket_parts():
    return "payload, propellant, structure"

output = rocket_parts()
print( output )    

# Un ejemplo de una función integrada que requiere un argumento es any(). Esta función toma un objeto iterable (por ejemplo, una lista) y devuelve True si algún elemento del objeto iterable es True. De lo contrario, devuelve False.
print ( any([True, False, False])  )
print ( any([False, False, False])  )
# >>> any()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: any() takes exactly one argument (0 given)


# Puede comprobar que algunas funciones permiten el uso de argumentos opcionales mediante otra función integrada denominada str(). Esta función crea una cadena a partir de un argumento. Si no se pasa ningún argumento, devuelve una cadena vacía:
print ( "label: ",str()   )
print ( "label: ",str(15) )

# Uso de argumentos de función en Python
def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"

# >>> distance_from_earth()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: distance_from_earth() missing 1 required positional argument: 'destination'


# Python genera TypeError con un mensaje de error que indica que la función requiere un argumento denominado destination. Si se pide al equipo del cohete que calcule la distancia del viaje con un destino, debe solicitar que un destino es un requisito. El código de ejemplo tiene dos rutas de acceso para una respuesta, una para la Luna y la otra para cualquier otra cosa. Use la Luna como entrada para obtener una respuesta:

print(  distance_from_earth("Moon")     )
print(  distance_from_earth("Saturn")   )

# Varios argumentos necesarios
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24
print(  days_to_complete(238855, 75)    )

# Funciones como argumentos
total_days = days_to_complete(238855, 75)
print(  round(total_days)   )

# Uso de argumentos de palabra clave en Python

from datetime import timedelta, datetime
def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print( arrival_time()  )
print( arrival_time(hours=0) )

# Combinación de argumentos y argumentos de palabra clave
from datetime import timedelta, datetime
def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")
# print(  arrival_time()  )
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: arrival_time() missing 1 required positional argument: 'destination'

print(  arrival_time("Moon")    )
print(  arrival_time("Orbit", hours=0.13)   )


# Uso de argumentos de variable en Python
# Cuando se usan argumentos de variable, a cada valor ya no se le asigna un nombre de variable. Todos los valores ahora forman parte del nombre de variable catch-all que usa el asterisco (en estos ejemplos, args).
def variable_length(*args):
    print(args)

variable_length()               # ()
variable_length("one", "two")   # ('one', 'two')
variable_length(None)           # (None,)

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
    
print(  sequence_time(4, 14, 18)    )#'Total time to launch is 36 minutes'  
print(  sequence_time(4, 14, 48)    )#'Total time to launch is 1.1 hours'

# Argumentos de palabra clave variable
# Al igual que con los argumentos de variable, no es necesario usar kwargs cuando se usan argumentos de palabra clave variable. Puede usar cualquier nombre de variable válido. Aunque es habitual ver **kwargs o **kw, debe intentar usar la misma convención en un proyecto.
def variable_length(**kwargs):
    print(kwargs)
variable_length(tanks=1, day="Wednesday", pilots=3)

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")
crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")     
# 3 astronauts assigned for this mission:
#       captain: Neil Armstrong
#       pilot: Buzz Aldrin
#       command_pilot: Michael Collins   

# Dado que puede pasar cualquier combinación de argumentos de palabra clave, asegúrese de evitar palabras clave repetidas. Las palabras clave repetidas producirán un error:
crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", pilot="Michael Collins")
#   File "<stdin>", line 1
# SyntaxError: keyword argument repeated: pilot