fruits = ("grapes","apples","berries")
animals = tuple(("lion","tiger","bear"))
for x in fruits:
    print(x)

print(fruits[2])

print(animals)
print(len(animals))
'''
#doesn't work

animals.add("dog")
print(animals)
animals[0] = "cheetah"
print(animals)
'''
del animals
print(animals)