def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height {height}, Weight {weight}, iq {iq}")

# A puzzle for an extra credit, type it anyway.
print("Here is a puzzle.")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

print(" ")

def what(a, b, c, d):
    return a + b - c * d / 2

what = what(age, height, weight, iq)

print("That becomes: ", what, "Can you do it by hand?")

print(" ")

#24 + 34 / 100 - 1023
what = substract(add(24, divide(34, 100)), 1023)

print("That becomes: ", what, "Can you do it by hand?")

print(" ")

a = float(input("Input a: "))
b = float(input("Input b: "))

a = add(a, b)
print(a)
a = substract(a, b)
print(a)
a = multiply(a, b)
print(a)
a = divide(a, b)
print(a, "\n")

c = add(a, b)
print(c)
c = substract(a, b)
print(c)
c = multiply(a, b)
print(c)
c = divide(a, b)
print(c)
