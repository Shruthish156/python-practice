#LOOPS CONCEPTs
#Loops means repeatedly  execution of the  program untill the condition become false :
#WHILE LOOP(condition based)
num=2
while num<8:
    print(num)
    num+=2

#print even number from 3 to 30
num=int(input("enter a number: "))
while num<=30:
    if num%2==0:
        print(num)
    num=num+1

#print tables use while loops
num=int(input("enter a number: "))
while num<11:
    print(f"2 x {num}={2*num}")
    num=num+1
#FOR LOOP
#DIFFERENCE OF WHILE LOOP AND FOR LOOP
# WHILE LOOP                                  #FOR LOOP
#1.it is manual control                       #1.it is automatic control
#2.it is indefinite iteration                 #2.it is definite iteration
#3.mainly use for unknown timings             #3.mainly use for known timings
#4.it is condition based                      #4.it is sequence based 

#FOR LOOPS
for i in range(5):  #from 0 to 1
    print(i)

name=input("enter a person name:")
for char in name:
    print(char)

#BREAK AND CONTINUE STATEMENTS
#break means : it is break down the current iteration or stop the program based on condition
#continus statements: skip the current iteration and then move to the nxt iteration
int=input("enter a person name : ")
for char in name:
    if char=="i":
        continue
    elif char=="a":
        break
    else:
        print("invalid:")
#pRINT TABLES
for i in range(2,4):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
    print()                         #this means it print new line 

#Pattern printing
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

print()

#reverse pattern
for i in range(5,0,-1):           #outer loop
    for j in range(i):            #inner loop
        print("*",end=" ")
    print()

print()
#print number pattern from 0
n=6
for i in range(1,n):           #outer loop only decide how many rows .it will decide
    for j in range(i):         #inner loop is mainly work for the entire program what will print
        print(j,end=" ")
    print()

print()
#print square pattern
num=6
for i in range(1,num):
    for j in range(1,num):
        print("*",end=" ")
    print()


print()
#print pyramid pattern
#it involve three logics 
#1.control or allocate thr rows
n=7
for i in range(1,n):
    for j in range(n-i):     #2.this for spaces allocation
        print(" ",end=" ")   #print spaces
    for j in range(2*i-1):   #this for pattern allocation
        print("*",end=" ")   #print spaces
    print()

print()
#reverse pyramid
n=7
for i in range(n,1,-1):       #this for control the repitatioon for the rows
    for j in range(n-i):   #thids is for spaces
        print(" ",end=" ")
    for j in range(2*i-3):
        print("*",end=" ")
    print()
   
     
