#FUNCTION
#it denoted as use def
#function means repited use of the block of code or reuse of the code
#it will save the time and eforts
#without use of return 
def add(a,b):   #step 1.define the function a,b are the parameters
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
add(5,6)        #step 2.calling the function 5,6 are the arguments
def greet(name,message):
    print(f"welcome to the {name} function for {message}")
greet("python","skilled enginners")
print()
#with use of return function
def multiplication(table,n):                     # step 1function defining
    return f"{table} X {n}={table*n}"            #step 5. return the values and print it
for n in range(1,11):                            #step 2.enter a loop
    result=multiplication(5,n)                   #step 3.function calling
    print(result)
print()
def num(getnum,totalnum):
    return (getnum/totalnum)*100
obtained_percentage=num(98,100)
print(f"the percentage of the person is : {obtained_percentage}")
print()
#print the tables from 2 to 4
def tables(i,j):
    return f"{i} X {j}={i*j}"
for i in range(2,5):
    for j in range(1,11):
        out_put=tables(i,j)
        print(out_put)
    print()
