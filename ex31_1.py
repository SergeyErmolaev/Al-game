print("Input a number from 1 to 10")
number = int(input("> "))

if number in range(1, 6):
    print("You choosed number between 1 and 5.")
    if number == 1:
        print("The number is 1")
    elif number == 2:
        print("The number is 2")
    elif number == 3:
        print("The number is 3")
    elif number == 4:
        print("The number is 4")
    elif number == 5:
        print("The number is 5")
    else:
        print("Your number is out of a range between 1 and 5")

elif number in range(6, 11):
    print("You choosed number between 6 and 10.")
    if number == 6:
        print("Tne number is 6")
    elif number == 7:
        print("The number is 7")
    elif number == 8:
        print("The number is 8")
    elif number == 9:
        print("The number is 9")
    elif number == 10:
        print("The number is 10")
    else:
        print("Your number is out of a range between 6 and 10")

else:
    print("Your number is out of a range")
