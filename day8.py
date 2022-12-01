@@ -0,0 +1,30 @@
n=5
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1,n-i,n-j), end=" ")
    print()

print()


n=5
for i in range(n):
    for j in range(n):
        print(max(i,j), end=" ")
    print() 

print()

n=5
for i in range(n):
    for j in range(n):
        print(max(n-j-1,n-i-1), end=" ")
    print()

print()

n=5
for i in range(n):
    for j in range(n):
        print(max(i,j,n-i-1,n-j-1), end=" ")
    print()