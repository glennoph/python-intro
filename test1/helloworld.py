#import sys
import os

print("hello world")

# this is a line comment

'''' 
multiline 
comment
with triple single quotes
'''
# Variables

# variable names start with char/letter followed by num or underscore
my_name = 'joe'

my_name_multiline = '''joe,
esquire'''

print(my_name_multiline)

print("%s %s" % ("mr", my_name) )

# Lists

items = ['apples', 'oranges', 'eggs']

print('first item[0] ', items[0])

print('num items ', len(items))

# append to list

items.append('milk')
print('append milk: ', items)

# sort list
items.sort()
print('sorted list ', items)

# first item
print('first item ', min(items))
# last item
print('last item ', max(items))

# slice first 2 items
print('first 2 ', items[:2])

# slice last 2 items
print('first 2 ', items[2:])

# extend
items_extra = ['bread', 'roles']
items.extend(items_extra)
print('extend items ', items)

# Tuple (immutable)

count_tuple = (0,1,2,3,4)
print('count_tuple ', count_tuple)
count_list = list(count_tuple)
count_list.append(5)
print('count_list ', count_list)
count_tuple5 = tuple(count_list)
print('count_tuple5 ', count_tuple5)

print('len min max ', len(count_tuple5), min(count_tuple5), max(count_tuple5))

# Dictionaries Map 

print('map tbd')

prices = {'apple': 11, 'oranges': 13, 'egg': 5}

print('prices dict ', prices)

prices['bread'] = 33

print('add bread/33 ', prices)

print('get price of bread= ', prices['bread'])
print('len prices= ', len(prices))
