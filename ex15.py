from sys import argv# import module

script, filename = argv #create varables

txt = open(filename)#open file

print(f"Here's your file {filename}:")# uotput some text
print(txt.read())#reads and outputs the contents of the file. Распечатывает прочитанный файл.

print("В каком режиме открыт ", txt.mode)
txt.close()
print("имя файла ", txt.name)
print("Файл закрыт ", txt.closed)

#print("Пробелы ", txt.softspace) didn't work

print("Type the filename again:")# output some text before input
file_again = input("> ") # input some text

txt_again = open(file_again)# open file

print(txt_again.read())# read opened file
print("Файл закрыт", txt_again.closed)

txt_again.close()
print("Файл закрыт", txt_again.closed)
