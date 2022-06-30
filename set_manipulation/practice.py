''' operations on sets '''
# creation of set
numSet = {1, 2, 3}
secondSet = {'one', 'two', 'three'}
print(numSet)

# check type
print(type(numSet))

# set union operator
print(numSet | secondSet)  # we can even write "numSet.union(secondSet)"

# set intersection operator
print(numSet & secondSet)  # we can even write "numSet.intersection(secondSet)"

# set difference operator
print(numSet - secondSet)  # we can even write "numSet.difference(secondSet)"

# set symmetric difference operator
# we can even write "numSet.symmetric_difference(secondSet)"
print(numSet ^ secondSet)

# frozenset
# we can even write "numSet.symmetric_difference(secondSet)"
numDict = {"one": 1, "two": 2, "three": 3}
numKeys = frozenset(numDict)
print(numKeys)
