#variable arguments in function 
#*arg
#it is use to passes the many arguments foe calculation or any in usually one parameter
def number(*nums):
#we do easy to sum all numbers bcz used *args other wise not sum all arguments in one parameter
    total=sum(nums)
    return total
result=number(1,2,3,4,7)
#caling the function
print(result)

#**kwargs (keyword arguments)
#it is use to passes the many key word arguments in one parameter
def person_profile(**student):
#fumction defining and passes the key word arguments
    return student
result=person_profile(name="shruthisha",age=20,work="BE",company="Google",skill=20)
#function calling
print(result)
#it print as dictionary key value pairs

#use both *arguments and **key word arguments 
def company_profile(*args,**kwargs):
    return args,kwargs
result=company_profile(company="google",role="software",degree="BE")
print(result)

#Lambda function
#it is anonymous function we take any number of arguments  in one expression
#syntax  :   lambda arguments : expression 
add=lambda a,b : a+b
print(add(1,5))

double= lambda x: x*2
print(double(5))








