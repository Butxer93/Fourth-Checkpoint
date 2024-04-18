from decimal import Decimal
from math import sqrt
import math

# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

my_list = ['Ibon', 'Markel', 'Irantzu', 'Aitor']  
my_tuple = ('PHP', 'Python', 'Java', 'CSS')
my_float = 34.56
my_integer = 58
my_decimal = Decimal(3/7)
my_dictionary = {
    'Name': 'Ibon',
    'Age': 30,
    'Country': 'Spain',
    'City': 'Bilbo'
}

# Exercise 2: Round your float up.

print(math.ceil(my_float))

# Exercise 3: Get the square root of your float.

print(sqrt(my_float))

# Exercise 4: Select the first element from your dictionary.

print(list(my_dictionary)[0])

# Exercise 5: Select the second element from your tuple.

print(my_tuple[1])

# Exercise 6: Add an element to the end of your list.

my_list.extend(['Itziar'])
print(my_list)

# Exercise 7: Replace the first element in your list.

my_list[0] = 'Elena'
print(my_list)

# Exercise 8: Sort your list alphabetically.

my_list.sort()
print(my_list)

# Exercise 9: Use reassignment to add an element to your tuple.

my_tuple += ('C++',)
print(my_tuple)
