# classes define the state and the behavior of the object

### Class Attributes (CA):
# takes place before the __init__ method
# They belong to the class.
# There is only one copy of each class attribute.
# Changing their value affects all instances since they all take the value from the same source.

### Instance Attributes (IA):
# They belong to the instances.
# Each instance has a separate copy of each instance attribute.
# Changing their value only affects a particular instance and the others remain unchanged.


class House:
    def __init__(self, price):  # init method of the class
        self.price = price  # first price is the attribute of the instance, self refers to the instance,


class Backpack:
    def __init__(self):
        self.items = []  # 'items' attribute for 'Backpack' class is empty list
        print self


my_backpack = Backpack()  # 'my_backpack' instance, it stores 'Backpack' object
print my_backpack  # same as 'print self'
print (type(my_backpack))  # instance
print "-----------------"


class Backpack_2:
    def __init__(self, color="blue", size="5"):
        self.items = []  # items attribute for backpack is empty list
        self.color = color
        self.size = size


your_backpack = Backpack_2()
print your_backpack.color
print "-----------------"


class Dog:
    species = 'Canis lupus'     # class attribute
    species_count = 1           # class attribute

    def __init__(self, name, age, breed):
        self.id = Dog.species_count
        self.name = name
        self.age = age
        self.breed = breed

        Dog.species_count += 1


print Dog.species_count  # it is '1' because printed before instances were created

my_dog = Dog('cookie', '5', 'doberman')
your_dog = Dog('spoon', '3', 'poodle')

print Dog.species
print my_dog.breed
print Dog.species_count  # it is '3' because printed after instances were created
print my_dog.id
print your_dog.id
print "-----------------"

