''' functions manipulation '''

# create a function


def greetings():
    print("Hello Py")


greetings()

# a function with parameter(s)


def welcomeAPythonista(name):
    print(f"Hello {name} in family of pythonistas, hope you willing to become a pythoneer or ML Engineer as our ambition")


welcomeAPythonista("Jules")

# a function with return type


def sum(a, b):
    return a+b


print(sum(4, 5))

# a function with default param(s)


def toBase(value, base=2):
    cases = {
        2: bin(value),
        8: oct(value),
        16: hex(value)
    }

    return cases.get(base, "Didn't operate on this base")


print(toBase(5))
print(toBase(5, 7))

# a function to return multiple values (returns a tuple of values)


def cube(side):
    volume = side ** 3
    surface_area = 6 * (side**2)
    return volume, surface_area


print(cube(8))

# a function with multiple unknown length params


def maxOfYourValues(*values):
    max_value = None

    for value in values:
        if (max_value is None or value > max_value):
            max_value = value
    return max_value


print(maxOfYourValues(5, 3, 33, 1, 36, 34634, 32))
