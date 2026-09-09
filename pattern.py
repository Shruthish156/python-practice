print("="*20)
print("NUMBER PATTERN:")
print("="*20)
n=int(input("enter a number: "))
for i in range(1,n):          #it allocate the rows and control the repitation
    for j in range(1,i+1):    #it is print the patterns
        print(j,end=" ")
    print()                   #new line of each iteration

print()
#print star pattern of triangle
n=7
for i in range(1,n):
    for j in range(i):
        print("*",end=" ")
    print()

print()
#reverse pattern of triangle
n=6
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print()
#print square pattern
n=6
for i in range(1,n):
    for j in range(1,n):
        print("*",end=" ")
    print()

print()
#print pyramid patter
n=7
for i in range(1,n):        #this for allocation and control the repitation of rows
    for j in range(n-i):    #this for spaces
        print(" ",end=" ")
    for j in range(2*i-1):  #this for print patterns
        print("*",end=" ")
    print()

print()
#reverse pyramid pattern
n=6
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()