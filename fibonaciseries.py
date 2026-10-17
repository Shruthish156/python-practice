#fibonaci series
#it means the adding of the current values and before values it give after nxt fibonaci values.
#0,1,1,2,3,5,8,13,21,34,55,------

#define the function
def fibonaci_values(n):
    if n==0:               #base case 1
        return 0
    if n==1:               #base case 2
        return 1
    #function call itself
    return fibonaci_values(n-1) + fibonaci_values(n-2)             #recursive call
#call the function
print(fibonaci_values(10))