#recursion
#recursion means it is process where function is call itself

#define the function
def value(n):
    #check the condition
    if n%4==0:                    #base case
        print(f"even number:{n}")
        return                    #stop the function
    print(n)
    value(n-2)                    #calling by itself
#calling the function
value(10)