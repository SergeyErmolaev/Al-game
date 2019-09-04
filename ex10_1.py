tabby_cat = "{}I'm tabbed in.".format('\t')
persian_cat = "I'm split {}on a line".format('\n')
backslash_cat = "I'm {} a {} cat".format("'", "\\")

fat_cat = '''
I'll do a{} list:
{} Cat food
{} Fishies
{} Catnip{} Grass
'''.format('\f', '\t*', '\t*', '\t*', '\n\v*')

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
