mycar = {
    "brand": "Range Rover Sports",
    "model": "HSE",
    "year": 2017
}
print(mycar)

mygreens = dict(fruit="green apples", vegetables="kale")
print(mygreens)
print(mygreens.get("fruit"))
print(len(mycar))

mycar["year"] = 2019
print(mycar)
mycar.update({"color": "silver"})
print(mycar)

b = mycar.keys()
print(b)

mycar.pop("color")
print(mycar)
del mycar["year"]
print(mycar)
mycar.clear()
print(mycar)
del mycar
#print(mycar) doesn't work


