
numbers = []

size_list = int(input("Input size list: "))
increment = int(input("Input increment: "))

def convent_list(size_list, increment):
    i = 0

    while i < size_list:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom is {i}")

    #return numbers

convent_list(size_list, increment)

print("The numbers: ")

for num in numbers:
    print(num)
