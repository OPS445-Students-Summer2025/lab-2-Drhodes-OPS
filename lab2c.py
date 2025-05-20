#!/usr/bin/env python3

#Name = input('Name: ')
#Age = input('Age: ')

#print('Hi ' + Name + ', you are ' + str(Age) + ' years old.')

import sys

name = sys.argv[1]
age = sys.argv[2]

print('Hi ' + name + ', you are ' + str(age) + ' years old.')