#factorial number

#define the function
def factorial(n):
    #it will ceck the condtion if n values is 1 it will return value 1
    if n==1:            #base case
        return 1 
    #function call by itself
    return n*factorial(n-1)     #recursive case .
    
print(factorial(9))