people = 15 # assigning a variable to a value
cars = 20 # assigning a variable to a value
trucks = 30 # assigning a variable to a value


if cars > people: # if function
    print("We should take the cars.")
elif cars < people: # another if function provided that the first is not True
    print("We should not take the cars.")
else:
    print("we can't decide.")

if trucks > cars or trucks > people:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
