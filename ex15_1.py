print('Type your file name:')
filename = input("> ")

txt = open(filename)#open file

print(f"Here's your file {filename}:")# uotput some text
print(txt.read())#reads and outputs the contents of the file

print("Type the filename again:")# output some text before input
file_again = input("> ") # input some text

txt_again = open(file_again)# open file

print(txt_again.read())# read opened file
