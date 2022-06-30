''' operations on strings '''
str = "hello world"
print("Hello world")

# print letter
print(str[1])

# print length of string
print(len(str))

# search in a string
print(str.count("l"), str.count(" "))
print(str.find("h"))
print(str.index("world"))

# string slicing
print(str[0:3])  # get the first three char
print(str[:3])  # get the first three char
print(str[-3:])  # get the last three char
print(str[3:])  # get all from 3rd index character
print(str[:-3])  # get all except three last characters

# splitting string
print(str.split(' '))

# startwith/endwith
print(str.startswith("H"))
print(str.endswith("d"))

# repeat string
print(str[:6] + str[6:]*3)

# replacing substring
print(str.replace("hello", "Hi"))

# changing cases of string
print(str.upper())
print(str.lower())
print(str.title())
print(str.capitalize())
print(str.swapcase())

# reversing string characters
print("".join(reversed(str)))

# strip string
word = " greetings here "
print(word.strip())
print(word.lstrip())
print(word.rstrip())

# string concatenation
print("2 + 3 = " + "5")

# join characters of string
print("-".join(word))

# truth value testing
print(word.isalnum())  # check if all char are alphanumeric
print(word.isalpha())  # check if all char in the string are alphabetic
print(word.isdigit())  # test if string contains digits
print(word.istitle())  # test if string contains title words
print(word.isupper())  # test if string contains upper case
print(word.islower())  # test if string contains lower case
print(word.isspace())  # test if string contains spaces
print(word.endswith('d'))  # test if string endswith a d
print(word.startswith('H'))  # test if string startswith H
