#String data type

#Literal assignment
from doctest import debug
from operator import truediv
from os import linesep

#from network import betweenness_centrality_subset


first = "Enos G."
last = "Mowatt"

#print(type(first))
#print(type(last) == str)
#print(isinstance(first,str))

# constructor function 
#pizza = str("pepperoni")
#print(type(pizza))
#print(type(pizza) == str)
#print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)


First = 'Enos'
last = 'Mowatt'
print(fullname)

statement = "I like reggae from the " + decade + "s."
print(statement)

# Multiple  Lines
multiline = '''
Hey, how are you ?

I was just checking in.   
                      All great here.

'''
print(multiline)

#Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located ?'
print(sentence)

#String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                       "
multiline =  "                    " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

#Build aMenu
title = "menu".upper()
print(title.center(20, "="))
print("coffee".ljust(16, ".") +  "$1".rjust(4))
print("Muffin".ljust(16, ".") +  "$6".rjust(4))
print("Bread".ljust(16, ".") +  "$5".rjust(4))
print("Cheesecake".ljust(16, ".") +  "$2".rjust(4))
print("")
# Strings Index Values

print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some method return boolean data
print(first.startswith("E"))
print(first.endswith("s"))
print("o" in first)

#Boolean data Types
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue,bool))

#Numeric data types

#Integer Types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price,int))

#Float Types

gpa = 3.28
y = float(1.4)
print(type(gpa))

# ComplexTypes
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in function for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa,1))

import math
print(math.pi) 

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#casting a string to number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt cast the wrong value
#zip_value = int("New York")