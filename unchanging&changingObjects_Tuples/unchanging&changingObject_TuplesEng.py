# os - library for working with the console
# random - library for working with random data

import os
import random

# Let's set the console font color to blue
os.system('COLOR B')

LEFT = 0  # LEFT - the left border
RIGHT = 20  # RIGHT - the right border
TYPE_COUNT = 10  # TYPE_COUNT - number of data types
MULTIPLIER = 100  # MULTIPLIER - multiplier

LEFT0 = ord('A')  # LEFT0 - character code A
RIGHT0 = ord('Z')  # RIGHT0 - character code Z
LEFT1 = ord('a')  # LEFT1 - character code a
RIGHT1 = ord('z')  # RIGHT1 - character code z
LEFT2 = ord('А')  # LEFT2 - character code А
RIGHT2 = ord('я')  # RIGHT2 - character code я

# Types of data
# int, float, complex, str, bool
# list, tuple, dict, set, frozenset

immutable_var = []  # immutable_var - the tuple
mutable_var = []  # mutable_var - list
RANGE = random.randint(LEFT, RIGHT)  # RANGE - the range
INTERVAL = random.randint(LEFT, RIGHT)  # INTERVAL - interval

for i in range(INTERVAL):
    RANGE = random.randint(LEFT, RIGHT)

    integer = random.randint(LEFT, RIGHT)
    # integer - an integer number
    double = random.random() * MULTIPLIER
    # double - a real number
    comp = complex(random.random() * MULTIPLIER,
                   random.random() * MULTIPLIER)
    # comp - a complex number
    boolean = bool(random.choice([0, 1]))
    # boolean - logical value
    string = ''.join([random.choice([
        random.choice([
            chr(random.randint(LEFT0, RIGHT0)),
            chr(random.randint(LEFT1, RIGHT1))
        ]),
        chr(random.randint(LEFT2, RIGHT2)),
        ' ',
        '.',
        ';',
        ',']
    )  # string - line
        for _ in range(RANGE)])

    info = [integer, double, comp, string, boolean]
    # info - list of various data
    lis = list([random.choice(info) for _ in range(RANGE)])
    # lis - list of various data
    tup = tuple([random.choice(info) for _ in range(RANGE)])
    # tup - a tuple of different data
    dictionary = dict(
        (random.choice(info[:len(info) - 2]), random.choice(info)) for _ in range(RANGE)
    )
    # dictionary - dictionary of various data
    sets = set([random.choice(info) for _ in range(RANGE)])
    # sets - lots of different data
    frozensets = frozenset([random.choice(info) for _ in range(RANGE)])
    # frozensets - a fixed set of different data

    data = [
        integer,
        double,
        comp,
        boolean,
        string,
        lis,
        tup,
        dictionary,
        sets,
        frozensets
    ]
    # data - a list of different data types and structures

    immutable_var.append(random.choice(data))  # filling out the tuple
    mutable_var.append(random.choice(data))  # filling out the list

immutable_var = tuple(immutable_var)
# converting from a list to a tuple

# We display information about the tuple and the list
print('\nINFORMATION ABOUT THE TUPLE AND THE LIST:\n')
print('The tuple:', immutable_var, end='.\n')

try:
    index = random.randint(LEFT, RIGHT)
    # index - random index
    immutable_var[index] = random.choice(data)
    # trying to change the tuple
    # the refusal to change is due to the presence of
    # fixed memory
except:
    print('An attempt to change the tuple!\n')

print('List:', mutable_var, end='.\n')
size = mutable_var.__len__()  # size - mutable_var size

for i in range(size):
    mutable_var[i] = random.choice(data)
    # filling in mutable_var

print('Modified list:', mutable_var, end='.\n\n')

try:
    os.system('PAUSE')  # Stopping the program
    os.system('CLS')  # Clearing the console screen
except:
    os.system('CLS')  # Clearing the console screen
