@@ -0,0 +1,59 @@
#looping statements

#while loop

a=1
while a<10:
    print(a)
    a += 1  #a = a + 1




#for loop

#every object in python can be sequence or not a sequence    
#iter method will tell us that expression is sequence
print(iter("s"))

name="jake"
print(type(name))

for a in name:
    print(a)
    print(type(a))


for i in range (7):
    print(i)




#break,continue and pass

for i in range(5):
    print(i)
    if i==3:
        break

for i in range(5):#i = 0
    print(i)#i = 0
    i = 100#i = 100
    print(i)#i = 100

for i in range(5):
    print(i)
    if i==3:
        continue

if True:
    pass
print("rest of the code")

for i in range(5):
    print(i)
    if i==3:
        break
else:
    print("invalid")    