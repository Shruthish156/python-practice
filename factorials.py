#factorial number

#define the function
def factorial(n):
    #it will ceck the condtion if n values is 1 it will return value 1
    if n==1:            #base case
        return 1 
    #function call by itself
    return n*factorial(n-1)     #recursive call.
    
print(factorial(9))

#sum of numbers
def sum(n):
    if n==1:       #base case
        return 1
    return n+sum(n-1)    #recursive call
print(sum(5))

#sum of digit
def sum_digit(digit):
    if digit==1:
        return 1
    #it will divide the digit by 10 give remeinder and do floor divisin give quotient
    return digit % 10 +sum_digit(digit//10)
print(sum_digit(1234))

