@@ -0,0 +1,80 @@
#Operators

#Arithmetic Operators

#Addition
from abc import abstractmethod


print(3+2)

#Subtraction
print(3-2)

#Division
print(3 / 2)

#Floor Division
print(3 // 2)

#Multiplication
print(3 * 2)

#Exponent
print(3 ** 2)

#Modulus
print(3 % 2)

#String concatenation
print("h"+"i")
print("hello" " " "world")

#string multilplication
print("hi"*3)



#Comparison operators

#Equal : ==
print(3==2)

#Not Equal : !=
print(3!=2)

#Less Than : <
print(3<2)
print("ab"<"x")#lexicographical comparison
print("S"<"s")

#Greater Than : >
print(3>2)

#Less or Equal : <=
print(3<=2)

#Greater or Equal : >=
print(3>=2)



#Logical operators
#not,and,or

print(True and False)
print(True or False)
print(True and 1)
print(1 and 0)
print(1 and 5)
# 0 is falsy
# 1 and other integers are truthy

#true or b = true
#false or b = b
#true and b = b
#false and b = false

print(6 or sam)
print(""and 1.2)
print(1.2 or"")