def hello_World():
    print("Hello World")


hello_World()


#
#
def sum(x, y):
    return x + y


print(sum(4, 3))
print(sum(8, 4))


#
#
def student_names(names="Bob"):
    print("Hello ", names)


student_names()
student_names("John")
student_names("Jane")


#
#
def more_num(a, b=7, c=10):
    print("a is ", a, "and b is ", b, "while c is ", c)


more_num(3, 7)
more_num(23, c=17)
more_num(c=40, a=80)


#
# Defining a function in a function
def greeting():
    def say_hello():
        return "Hello"

    return say_hello()


hello = greeting()
print(hello)


#
#
def mynum(x):
    return x + 1


num = mynum
num2 = mynum(5)
print(num(7))
print(num2)


#
# Pass Statement
def dream_home():
    pass


dream_home()


#
# Passingg Functions as Arguments to other Functions
def mynum(b):
    return b + 1


def addnum(c):
    newnum = 7
    return c(newnum)


print(addnum(mynum))


#
# Variable Arguments
def total_numbers(a=22, *numbers, **phonebook):
    # *numbers is collected as a tuple.
    # **phonebook is collected as a dictionary
    print("My fav number is ", a)

    for num in numbers:
        print("num", num)

    for name, phone_number in phonebook.items():
        print(name, phone_number)


total_numbers(22, 1, 2, 3, Jane=2222, John=4444, Angela=5555)

#
# Anonymous functions
a = lambda b: b + 4
print(a(4))

c = lambda d, e: d + e
print(c(7, 8))


def ghost_number(n):
    return lambda f: f * n


double_num = ghost_number(2)

print(double_num(20))

''' Global vs local variables
'''
x = 10  # global variable


def my_numbers(x):
    print(x)
    x = 7  # local variable
    print("My fav number is ", x)


my_numbers(x)
print(x)


#
#
def my_numbers2():
    global x  # Call global variable
    print(x)
    x = 7
    print("My fav number is ", x)


my_numbers2()
print(x)


'''DocStrings
'''
def add_numbers(d,e):
    ''' Adding two numbers.

    The values must be integers
    '''
    print(d+e)
add_numbers(8,4)
print(add_numbers.__doc__)



