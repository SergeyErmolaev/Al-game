from sys import argv
# read the WYSS section for how to run this
script, first, second, third, fourth = argv

x = input("What is your name? ")
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("your fourth variable is:", fourth)
print(f"Your name is {x}")
