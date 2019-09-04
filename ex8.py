formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Humpty Dumpty sat on a wall,",
    "Humpty Dumpty had a great fall,",
    "All the king's horses and all the king's men",
    "Couldn't put Humpty together again."
))
