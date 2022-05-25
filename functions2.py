'''Nested Functions
'''

def mynum(a):
    def num(a):
        return a + 1
    print(a)
    result = num(a)
    print(result)
    return result

mynum(10)
#
#Accessing Variables from outer function. Called a closure
def display_message(message):
    "hello"
    def message_sender():
        "nested function"
        print(message)
    message_sender()

display_message("Show me the money!")


