i = 0

while i<8:
    i += 1
    if i%2 == 0:
        continue
    print(i)

fruits = ["grapes", "berries", "oranges"]

for x in fruits:

    if x == "berries":
        continue
    print(x)