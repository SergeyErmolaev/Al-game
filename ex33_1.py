numbers = []
size_list = int(input("Input size list: "))
increment = int(input("Input your increment: "))

def convent_list(size_list, increment):
    for i in range(0, size_list, increment):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom is {i + 1}")

convent_list(size_list, increment)

print("The numbers: ")

for num in numbers:
    print(num)
