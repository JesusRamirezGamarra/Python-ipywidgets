print( "temperatures and facts about the moon".title()  )

heading = "temperatures and facts about the moon"
print(  heading.title() )

temperatures = """Daylight: 260 F
... Nighttime: -280 F"""
print(  temperatures .split()   )

print(  temperatures .split('\n')   )
['Daylight: 260 F', 'Nighttime: -280 F']

print(  "Moon" in "This text will describe facts and challenges with space travel"   )
print(  "Moon" in "This text will describe facts about the Moon"    )


temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
print(      temperatures.find("Moon")   )
print(      temperatures.find("has")   )


temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
print(      temperatures.count("Moon")   )
print(      temperatures.count("has")   )

print(     "The Moon And The Earth".lower()  )
print(     "The Moon And The Earth".upper()  )

temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(  parts  )
print(  parts[-1]   )


mars_temperature = "The highest temperature on Mars is about 30 C, -40 C"
print(  mars_temperature    )
for item in mars_temperature.split():
    
    if item.isnumeric():
        print(item)
    elif item.startswith('-'):
        if item.split('-')[1].isnumeric():
            print(item)
        

print("-60".startswith('-')       )

if "30 C".endswith("C"):
    print("This temperature is in Celsius")

print   ("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C")    )


text = "Temperatures on the Moon can vary wildly."
print ( "temperatures" in text )
print ( "Temperatures" in text)



moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
print( '\n'.join(moon_facts) )


mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage)

#Formato de signo de porcentaje (%)
print("""Both sides of the %s get the same amount of sunlight,
... but only one side is seen from %s because
... the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))


#El método format()
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))

print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))

print("""You are lighter on the {moon}, because on the {moon} 
... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))

#Acerca de las cadenas f-strings
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")

print ( round(100/6, 1) ) 
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")

subject = "interesting facts about the moon"
print(  f"{subject.title()}" )

