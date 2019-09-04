from sys import argv#import module

script, filename = argv#create variables and assign values to them

print(f"We're going to erase {filename}.")# output some text with created veriable

print("Opening the file ...")#output some text
target = open(filename, 'w')#create a variable open the file in edit mode

print("Truncating the file. Goodbay!")#output some text
target.truncate()#truncates the file's size

print("Now I'm going to ask you for three lines.")# output some text

line1 = input("line 1: ")#input lines, create variables and assign values to them
line2 = input("line 2: ")#input lines, create variables and assign values to them
line3 = input("line 3: ")#input lines, create variables and assign values to them

print("I'm going to write these to the file.")#output some text

target.write("{}{}{}\n{}".format(line1,'\n', line2, line3))#write lines to a file


print("And finally, we close it.")#output some text
target.close()#close the file
