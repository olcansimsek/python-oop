# classes define the state and the behavior of the object


class House:
    def __init__(self, price):  # init method of the class
        self.price = price      # first price is the attribute of the instance, self refers to the instance,


class Backpack:
    def __init__(self, color, size):
        self.items = []         # items attribute for backpack is empty list
        self.color = color
        self.size = size
