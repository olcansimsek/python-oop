#!/usr/bin/python3

##########################################
# PYTHON 3 Only
##########################################

class Circle:
    VAILD_COLORS = ("Red", "Blue", "Green")

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and new_radius > 0:
            print ("setting new radius....")
            self._radius = new_radius
        else:
            print ("Please insert a valid radius!")

    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        print ("setting new color....")
        if new_color in Circle.VAILD_COLORS:
            self._color = new_color
        else:
            print ("Please insert a valid color!")

    color = property(get_color, set_color)


my_circle = Circle(10, "Blue")

print ("--- RADIUS ---")  # with the property, you can get and set a attribute by calling it with its name ??????
print (my_circle.radius)
my_circle.radius = 15
print (my_circle.radius)

print ("\n--- COLOR ---")  # with the property, you can get and set a attribute by calling it with its name ??????
print (my_circle.color)
my_circle.color = "ALPA"
print (my_circle.color)
print ("\n-----------------\n")


class Movie:

    def __init__(self, name, rating):
        self.name = name
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, int) and new_rating > 0:
            self._rating = new_rating
        else:
            print ("Please insert a valid rating!")


my_movie = Movie("Titanic", 4)

print (my_movie.rating)
my_movie.rating = "E"
print (my_movie.rating)
print ("\n-----------------\n")


class Circle:
    pi = 3.1416

    def __init__(self, diameter, color):
        self.diameter = diameter
        self.color = color

    def _get_radius(self):
        return self.diameter / 2

    def find_area(self):
        return Circle.pi * self._get_radius() ** 2  # call the class function


blue_circle = Circle(20, "Blue")
new_area = blue_circle.find_area()
print new_area
print ("\n-----------------\n")

