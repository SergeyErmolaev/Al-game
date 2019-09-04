print("""You enter a dark room with two doors.
Do you go through door #1, door #2 or door #3?""")

door = input('> ')

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into  the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("September is the mating period of the moose.")
    print("You're standing in front of the moose.")
    print("What do you do?")
    print("1. Try to escape.")
    print("2. Scream at the moose.")
    print("3. Tape your option")

    moose = input("> ")

    if moose == "1":
        print("Moose will break your head")
        print("Good job!")
    elif moose == "2":
        print("Moose will break your spine.")
        print("Good job!")
    else:
        print(f"Well, doing {moose} is probably better.")
        print("Moose runs away.")

else:
    print("You stumble around and fall on a knife and die. Good job!")
