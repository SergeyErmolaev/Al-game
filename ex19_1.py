def whiskey_and_soda(whiskey_bottles, soda_bottles):
    print(f"You have {whiskey_bottles} bottles of whiskey!")
    print(f"you have {soda_bottles} soda bottles!")
    print("That is enough for party!")
    print("Forward for the adventure!\n")

#1
print("We can give the finctions number directly:")
whiskey_and_soda(1, 2)

#2
print("OR, we can use varables from our script:")
amount_of_whiskey = 2
amount_of_soda = 5
whiskey_and_soda(amount_of_whiskey, amount_of_soda)


#3
print("We can use variables from input:")
amount_of_whiskey = int(input("Enter amount of whiskey:"))
amount_of_soda = int(input("Enter amount of soda:"))

whiskey_and_soda(amount_of_whiskey, amount_of_soda)


#4
print("We can do math inside:")
whiskey_and_soda(1 + 2, 2 + 5)


#5
print("We can use both, variables and math:")
whiskey_and_soda(amount_of_whiskey + 3, amount_of_soda + 7)


#6
print("We can use math for variablesfrom script and input")
amount_of_whiskey_from_James = int(input("Bottles from James:"))
print("Bottles of soda from Kelly;")
amount_of_soda_from_Kelly = int(input())
whiskey_and_soda(amount_of_whiskey + amount_of_whiskey_from_James, amount_of_soda + amount_of_soda_from_Kelly)


#7


#8


#9


#10
