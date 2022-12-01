@@ -0,0 +1,62 @@
# 1 indent = 2 spaces, 4 spaces , tab , 8 spaces


#Control Flow Statements

#Conditional Statements
a=False
if a:
    print("the value is true")
print("end")

a=1
if a==1:
    print("True")
else:
    print("False")


#Nested if-else
a=int(input("Enter no.: "))
if a<0:
    print("Integer is negative")
elif a==0:
    print("Neither positive nor negative")
else :
    print("Integer is positive")   


#k-map question


# q-can profile a access profile b
# a = isFriend
# b = isBlocked
# c = isAdmin
# d = isMarkZuckerberg

# a b c d q
# 0 0 0 0 0
# 0 0 0 1 1
# 0 0 1 0 1
# 0 0 1 1 1
# 0 1 0 0 0
# 0 1 0 1 1
# 0 1 1 0 0
# 0 1 1 1 1
# 1 0 0 0 1
# 1 0 0 1 1
# 1 0 1 0 1
# 1 0 1 1 1
# 1 1 0 0 0 
# 1 1 0 1 1
# 1 1 1 0 0
# 1 1 1 1 1        


a="is friend"
b="is blocked"
if a=="is friend":
    print("has access")
else:
    print("access denied")    