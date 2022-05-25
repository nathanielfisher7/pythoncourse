fruits = {"grapes","apples","berries"} #a set made using curly brackets
#for x in fruits:
#    print(x)

animals = (("lion", "tiger", "bear")) #also a set
#cannot index through set, but can use a for loop

#print(len(animals))
fruits.add("oranges")
print(fruits)

fruits.update(["melon", "blueberries"])
print(fruits)

fruits.remove("melon")
print(fruits)

fruits.clear()
print(fruits)

del animals
#print(animals) #doesn't work.