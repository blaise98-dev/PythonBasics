''' classes manipulation in python '''

# create a class


class MyClass:
    def __init__(self):  # constructor in py
        print("Hello ojects in python")


MyClass()

# create a class with methods (functions alias in classes)


class Cuboid:
    def __init__(self, length, breadth, height, weight):
        self.length = length
        self.breadth = breadth
        self.height = height
        self.weight = weight

    def volume(self):
        x = self.length
        y = self.breadth
        z = self.height
        v = x * y * z
        print("The volume is:", v)

    def density(self):
        x = self.length
        y = self.breadth
        z = self.height
        v = x * y * z
        d = self.weight / v
        print("Density is:", d)

    def surface_area(self):
        x = self.length
        y = self.breadth
        z = self.height
        s = 2 * (x * y + y * z + x * z)
        print("The surface area is:", s)


myCuboid = Cuboid(1, 2, 4, 4.5)
myCuboid.density()
myCuboid.surface_area()
myCuboid.volume()
