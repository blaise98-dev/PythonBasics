''' operations on tuples (immutable lists) '''
# creation of tuple
letters = ('a', 'e', 'i', 'o', 'u')
print(letters)

# creation of tuple from string
strToTuple = tuple("hello")
print(strToTuple)

# creation of tuple from input
inputToTuple = tuple(input("Write random numbers:\t"))
print(inputToTuple)

# accessing tuple items
print(letters[0::2])

# join tuples
consonants = ('b', 'c', 'd', 'f', 'g')
print(letters + consonants)

# tuple unpacking
(l1, l2, *l3) = letters
print(l3)
