#Taking Input in python
#input() function
#delimeter is only \n character

x=input("Enter input: ")
print(x)
print(type(x))

#Typeconversion
a=15
a=str(a)
print(a)
print(type(a))

b=float(4.35)
b=int(b)
print(b)
print(type(b))

#isinstance
a=45
print(isinstance(a,object))
a="A"
print(isinstance(a,object))