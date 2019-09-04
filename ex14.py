from sys import argv

script, user_name, age = argv
prompt = '>> '

print(f"Hi {user_name}, your age is {age}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)


print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"Where are you from {user_name}?")
native_place = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f'''
Alright, so you said {likes} about liking me.
You live in {lives}. not sure where that is.
You are from {native_place}.
And you have a {computer} computer. Nice.
''')

print('''
Alright, so you said {} about liking me.
You live in {}. not sure where that is.
You are from {}.
And you have a {} computer. Nice.
'''.format(likes, lives, native_place, computer))
