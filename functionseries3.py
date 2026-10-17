#nested function
#a function is contain inside another function is called as nested function.

#out side the function and define it
def student(name,marks,percentage): 
    #inside the function and define it          
    def company(role,salary):
        result_display=f"The student {name} he got {role} role with salary of {salary} per month"
        return result_display
    #calling the inside function
    print(company("AIeng",100000)) 
    marks_require=f"{name} got marks is : {marks} and percentage is : {percentage}"
    return marks_require
#calling the outside function
print(student("Shruthisha",552,92))

"""
=======The flow of the program====
1.first is define the outside function student() but not execute it
and move the below line of code and calling the function  based on parameters
2.after calling move to inside function company()
again it will define and calling it
nxt it will return the values of inside function
3.nxt move to return the outside function

"""
