#global and local variable 
#global variable : it is locate outside the function
x=10
#global variable 
def value():
    print(x)    
value()
print(x)

#local variable : it is locate inside the function

x=13
def value():
    x=12
    #local variable 
    print(x)  #it print 13
value()
print(x)      #it print 13 because it is global variable .outside use the print(inbuilt function)    

#when we decalre variable as global and use print inside and outside it print both local and global 
#when we decalre variable as local use print inside and outside it print only local not global it give error

# student marks calculator
print("=======STUDENT MARKS CALCULATOR======")
def total_marks(marks):
    total=sum(marks)
    return total
def average_marks(marks):
    average=sum(marks)/len(marks)
    return average
print(total_marks([98,85,75,68,88,86]))
print(average_marks([98,85,75,68,88,86]))

#number check even or odd
while True:
    def check_number(num):
        if num%2==0:
            return "even"
        else:
            return "odd"
    #ask the user for input
    num=int(input("enetr a number: "))
    print(check_number(num))
    again_check=input("do you again check the number: (yes/no)")
    if again_check=="no":
        break
#print number
def number(n):        
#defining
    return i
n=int(input("enter n :"))
for i in range(n,6):
    print(number(n))
    #calling

def number(nums):
    if nums%2==0:
        return f"the {nums} is even"
    else:
        return f"the {nums} is odd"
for nums in range(5):
    nums=int(input("enter a  numbers:"))
    print(number(nums))







