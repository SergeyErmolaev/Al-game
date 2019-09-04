from sys import exit

def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if is_number(choice):
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You're greedy bastard!")

def bear_moved_choice():
    bear_moved = True
    print("Take honey or taunt bear. What will you do?")
    choice = input("> ")

    if choice == "take honey":
        dead("The bear looks at you then slaps your face off.")
    elif choice == "taunt bear":
        if bear_moved:
            print("The bear has moved from the door.")
            print("You can go though it now.")
            print("Will you open the door?")
            choice = input("> ")
            if choice == "open door":
                gold_room()
            else:
                dead("The bear moves back, gets pissed off and chews your leg off.")
        else:
            dead("The bear gets pissed off and chews your leg off.")
    else:
        print("I got no idea what that means.")
        bear_moved_choice()

def bear_room():
    print("There is are bear here.")
    print("The bear has are bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")

    bear_moved_choice()


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
