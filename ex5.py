name = 'Zed A. Show'
age = 35 # noy a lie
height = 74 # inches
height_in_cm = round(height * 2.51, 2)#centimeters
weight = 180 # lbs
weight_in_kg = round((weight * 0.4536), 2) #kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about {}.".format(name))
print(f"He's {height} inches or {height_in_cm} centimeters tall.")
print(f"He's {weight} pounds or {weight_in_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair")
print(f"his teeth are usually {teeth} depending on the coffee")

#this line is tricky, try to get it exactly right
total = age + height + weight
total_metr = age + height_in_cm + weight_in_kg
print(f"If I add  {age}, {height}, and {weight} I get {total}. If I add {age}, {height_in_cm} and {weight_in_kg} I get {total_metr}")
