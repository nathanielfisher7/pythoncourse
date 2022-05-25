animals = ["bear", "tiger", "lion", "panda", "elephant"]
fruits = ["berries", "apples", "grapes", "oranges"]
vegetables = ["kale", "broccoli", "lettuce"]
'''
    for x in animals:
        print(x, "\n")
    print(animals)
    
    print(animals[0])
    print(animals[-1])
    print(animals[1:3])
    animals[0] = "dog"
    print(animals[0])
'''
fruits.extend(vegetables)
print(fruits)
vegetables.append("bean")
print(vegetables)
vegetables.sort()
print(vegetables)
vegetables.sort(reverse=True)
print(vegetables)

print(fruits.count("berries"))
print(fruits.index("berries"))
fruits.insert(2, "fish")
print(fruits)

fruits.pop()
print(fruits)

fruits.remove("apples")
print(fruits)

del fruits
print(fruits)

