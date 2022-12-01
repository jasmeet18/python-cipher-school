print("Hello World")

#This is a comment
#Every line executed in python is either a statement or a expression

#Python does not have character
a="a"
print(type(a))

#Four basic datatypes in python
 #integers
 #float
 #string
 #complex

#Everything in python isinstance of object
print(isinstance(a,object))

#limit of integer in python depends on RAM of the system
b=255
print(b)

#id function returns actual ram address
print(id(b))
print(hex(id(b)))

print(id(a))

#optimisation
c=200
d=200
print(id(c))
print(id(d))

#Variables(a type of identifier)
#some rules
 #first character must be alphabet(uppercase or lowercase) or underscore
 #variable name cannot start with a number
 #variable name are case-sensitive
 #variable name can contain only alpha-numeric and underscore

#Acceptable variable names

# myname = 'Peter'
# my_name = 'John'
# _my_name = 'John'
# myName = 'John'
# MYNAME = 'john'
# myname3 = 'john'

#Not Acceptable
# 2myname = 'John'
# my-name = 'John'
#  my name = 'John'