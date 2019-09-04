types_of_people = 10 #assign a value to the variable. number
x = f"There are {types_of_people} types of people."#assign a value to the variable, format the digit into a string and concatenate the strings

binary = "binary"#assign a value to the variable. string.
do_not = "don't"# assign a value to the variable. string.
y = f"Those who know {binary} and those who {do_not}." # assign a value to the varriable and concatenate them

print(x)#the output
print(y)#the output

print(f"I said: {x}")#concatenation
print(f"I also said: '{y}'")#concatenation

hilarious = True#assign bolean
joke_evaluation = "Isn't that joke so funny?! {}"#leave room for concatenation

print(joke_evaluation.format(hilarious))# output and concatenation

w = "This is the left side of ..."#assign a value to the concatenation
e = " a string with a right side."#assign a value to the concatenation

print(w + e + " " + joke_evaluation.format(hilarious))# concatenation
