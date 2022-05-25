class Cars:
    def __init__(self,speed,color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_color(self,value):
        self.__color = value

    def get_color(self):
        return self.__color


ford = Cars(250, "green")
nissan = Cars(300,"red")
toyota = Cars(350,"blue")

ford.set_speed(450)
ford.speed = 500
print(ford.get_speed())

print(ford.get_color())


