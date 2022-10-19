# open("/public/mars.jpg")


# # Imports PIL module 
# from PIL import Image
# # open method used to open different extension image file
# im = Image.open(r"D:\APP\python\microsoft\ipywidgets\src\public\mars.jpg") 
# # This method will show image in any image viewer 
# im.show() 



def main():
    try:
        configuration = open(".\src\public\mars.jpg")
        print(configuration)
        configuration.show()
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")        
#############################################################
# En este caso, as err significa que err se convierte en una variable con el objeto de excepción como valor. Después, usa este valor para imprimir el mensaje de error asociado a la excepción. Otra razón para usar esta técnica es acceder directamente a los atributos del error. Por ejemplo, si detecta una excepción OSError más genérica, que es la excepción primaria de FilenotFoundError y PermissionError, puede diferenciarlas mediante el atributo .errno:
    
def fileTxt():
    try:
        configuration = open('.\src2\config.txt')
        print(configuration)
    except FileNotFoundError as err:
        print("Couldn't find the config.txt file! ", err)
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")        
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")        
#############################################################
def fileTxtV2():
    try:
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")

if __name__ == '__main__':
    #main()
    #fileTxt() 
    fileTxtV2()
    
#############################################################    
loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""    

parsed_config = {}
for line in loaded_config.split('\n'):
    try:
        key, value = line.split('=')
        parsed_config[key] = value
    except ValueError:
        print(f'Unable to parse {line}')
print(parsed_config)
#############################################################
def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    return f"Total water left after {days_left} days is: {total_water_left} liters"    
print (     water_left(5, 100, 2)    )

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"
print(     water_left(5, 100, 2)    )

try:
    water_left(5, 100, 2)
except RuntimeError as err:
    alert_navigation_system(err)        
print(  water_left("3", "200", None) )


def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

print(  water_left("3", "200", None) )
# Traceback (most recent call last):
#   File "<stdin>", line 5, in water_left
# TypeError: unsupported operand type(s) for /: 'str' and 'int'

# During handling of the preceding exception, another exception occurred:

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 9, in water_left
# TypeError: All arguments must be of type int, but received: '3'