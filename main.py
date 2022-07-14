# classes define the state and the behavior of the object
# what is 'self': https://www.youtube.com/watch?v=oaiQ5hYKHTE&ab_channel=PythonForEveryone

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
    def __init__(self):  # 'self' meaning is instance itself, self = my_backpack python passes instance itself to the 'self'
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
        self.__lock = 38

        Dog.species_count += 1


print Dog.species_count  # it is '1' because printed before instances were created

my_dog = Dog('cookie', '5', 'doberman')
your_dog = Dog('spoon', '3', 'poodle')

print Dog.species
print my_dog.breed
print Dog.species_count  # it is '3' because printed after instances were created
print my_dog.species_count  # why '3' ??
print my_dog.id
print your_dog.id
print my_dog._Dog__lock  # you can print __lock because this attribute has a default vaule
print your_dog._Dog__lock
print "-----------------"


class Movie:
    def __init__(self, title, year):
        self._title = title
        self.rating = year

    def get_title(self):
        return self._title


my_movie = Movie("The Fall", 2006)

print my_movie.get_title()
print "-----------------"


class Cat:

    def __init__(self, name, age):
        self._name = name
        self.age = age

    def get_name(self):  # function object
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():  # check if new_name is string and alphabetic
            self._name = new_name
        else:
            print "The new name {0} is not a valid name!".format(new_name)


my_cat = Cat("Dora", 5)
print my_cat.get_name()

my_cat.set_name("Gora")
print my_cat.get_name()

my_cat.set_name("foo/bar")
print my_cat.get_name()
print "-----------------"


class Planet:

    def __init__(self, name, age):
        self.name = name
        self._age = age  # _age property itself

    def get_age(self):  # getter function
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int):  # check if new_age is integer
            self._age = new_age
        else:
            print ("Please insert a valid age!")

    age = property(get_age, set_age)  # property of getter and setter


planet_earth = Planet("earth", "5")

print planet_earth.name
print planet_earth.age          # this works when there is property of getter and setter
print planet_earth._age         # this works when you call _age property itself
print planet_earth.get_age()    # this works when there is getter function