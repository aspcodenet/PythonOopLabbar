# CONSTRUCTOR = anropas automatiskt när vi skapar ett sånt objekt
# SYFTE:    skapa upp properties (ritning)
#           initiera i valid state

class Rectangle:
    def __init__(self, width:int, height:int):
        self.__Width = width
        self.__Height = height

    def CalculateArea(self):
        return self.__Height * self.__Width

