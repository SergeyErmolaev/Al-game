def cheese_and_crackers(cheese_count, boxes_of_crackers): # It is function definition and variables creation
    print(f"You have {cheese_count} cheeses!")# This is function body that it performs.
    print(f"you have {boxes_of_crackers} boxes of crackers!")# This is function body that it performs.
    print("Man that's enough for party!", end = " ")# This is function body that it performs.
    print("Get a blanket.\n")# This is function body that it performs.


print("We can just give the function numbers directly:") # output some text
cheese_and_crackers(20, 30) # function call


print("OR, we can use variables from our script:") # output some text
amount_of_cheese = 10 # creating a variable and assigning a value to it.
amount_of_crackers = 50 # creating a variable and assigning a value to it

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # the function call


print("We can even do math inside too:")# output some text
cheese_and_crackers(10 + 20, 5 + 6) # the function call


print("And we can combine the two, variables and math:")# output some text
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # the function call
