
#all cars we havecars = 100
space_in_a_car = 4.0
#all drivers we have
drivers = 30
#all passengers we need to drive
passengers = 90
#cars without passengers
cars_not_driven = cars - drivers
#cars with driver , can be used
cars_driven = drivers
#number of passengers we can drive in total
carpool_capacity = cars_driven * space_in_a_car
#average passengers per car to drive them at a time
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers availiable.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")
