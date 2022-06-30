''' operations on lists (arrays in other pro langs) '''

# creation of list
colors = ['yellow', 'red', 'blue', 'green', 'black']

print(colors)

# operating on indexes
print(colors[2])
colors[1] = "gray"
print(colors)

# slicing on list
print(colors[1:4])
print(colors[2:])
print(colors[:2])
print(colors[-1])
print(colors[1:-1])

# get length of list
print(len(colors))

# sorting list (ascending and descending)
colors.sort()  # this mutate or change a list
print(colors)
print(sorted(colors))
print(sorted(colors, reverse=True))

# append item in a list
colors.append("pink")
print(colors)

# remove item from a list
colors.remove("gray")
print(colors)

# delete item from a list (use index instead of value)
del colors[0]
print(colors)

# delete item from a list (use index instead of value)
print(colors.pop(2))

# insert into list (it allows to insert item at a given index)
colors.insert(2, "white")
print(colors)

# extend list
otherColors = ["#333", "#111", "#454677"]
colors.extend(otherColors)
print(colors)

# use keyword "in" to check if item is in list
if 'white' in colors:
    print("white is there")

# loop through items of list
for color in colors:
    print(color, colors.index(color))
