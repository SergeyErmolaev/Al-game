from sys import argv # import argv module

script, input_file = argv # The list of command line arguments passed to a Python script

def print_all(f): # The function that reads and uotputs the contents of the "f" file
    print(f.read(), '\n')

def rewind(f):# The function that returns to the first line
    f.seek(0)

def print_a_line(line_count, f):#the function that prints the selected line of the file
    print(line_count, f.readline(), end='')

current_file = open(input_file)# assign a value of the build-in function that opens the file to the variable

print("First let's print the hole file:\n")# print the text in brackets

print_all(current_file)# print the text of the open file

print("Now let's rewind, kind of like a tape.")# print the text in brackets

rewind(current_file)# return the cursor to the beginning of the file

print("Let's print three lines:", '\n')# print the text in the brackets

current_line = 1 #assign a value to the variable
print_a_line(current_line, current_file) #call the function, specify the line number and the name of the opened file

current_line += 1 #assign a value to the variable
print_a_line(current_line, current_file) #call the function, specify the line number and the name of the opened file

current_line += 1 #assign a value to the variable
print_a_line(current_line, current_file) #call the function, specify the line number and the name of the opened file
print('\n')

current_file.seek(0)
print(1, current_file.readline())
print(2, current_file.readline())
current_file.seek(3)
print(3, current_file.readline())
