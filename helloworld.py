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

shopping_list = ['apples', 'oranges', 'eggs']

print('first item[0] ', shopping_list[0])

print('num items ', len(shopping_list))

# append to list

shopping_list.append('milk')
print('append milk: ', shopping_list)

# sort list
shopping_list.sort()
print('sorted list ', shopping_list)

# first item
print('first item ', min(shopping_list))
# last item
print('first item ', max(shopping_list))

# Tuple (immutable)

count_tuple = (0,1,2,3,4)
print('count_tuple ', count_tuple)
count_list = list(count_tuple)
count_list.append(5)
print('count_list ', count_list)
count_tuple5 = tuple(count_list)
print('count_tuple5 ', count_tuple5)

print('len min max ', len(count_tuple5), min(count_tuple5), max(count_tuple5))

# Map 

print('map tbd')

