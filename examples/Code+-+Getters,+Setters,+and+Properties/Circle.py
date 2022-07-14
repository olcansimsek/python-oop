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

print ("--- RADIUS ---")  # with the property, you can get and set a attribute by calling it with its name
print my_circle.radius
my_circle.radius = 15
print my_circle.radius


print ("\n--- COLOR ---")  # with the property, you can get and set a attribute by calling it with its name
print my_circle.color
my_circle.color = "Green"
print my_circle.color