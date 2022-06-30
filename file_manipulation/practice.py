''' files handling using python '''

# open a file in python
with open('../plain_texts.txt') as file:
    # print(file.read())
    print(file.readline(3))
    print(file.readlines())  # or file.list()
