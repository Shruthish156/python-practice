print("="*20)
print("python world !!!! ")
print("="*20)
print("====welcome to the world of python learning for AI engineering======")
print("hello world!!!")
#python is a high level,small code with interpretd versatile language and it is a dynamically typed language
#1.It has a rich library support
#2.small and efficient code
#3.use for AIautomation,ML,data ,etc===

#VARIABLES AND DATA TYPES
a,b,name,Name=12,12.5,"shruthisha",'R'
print(f"{type(a)},{type(b)},{type(name)},{type(Name)}") 
#In python there is no fixed size bytes stored comare to  c/c++ so use to check sys.getsizeof()

#THE POWER OF PRINT IT CONTAIN OBJECTS,SEP,END,FILE,FLUSH it is for bufferinf timings 
print("ramu","raju","summu",sep=" | ")       #separate
print("ramu","raju","summu",end=" ")         #end combining the below code wirh the current code
print("ravana")

#INPUT AND OUTPUT 
a=input("enter a boy name for gaming: ")  #it always be a string 
b=int(input("enter a number for playing a game : "))  #int 
print(a+str(b)) 
print(f"the person {a} is directly contact with shruthisha at the years of {b} years old")                            #concatenation of string 
name=int(input("enter a number: "))
Name=float(input("enter a number 2: "))
print(name+Name)

#STACK AND HEAP
x=10  #in this code x=store in stack and 10 is store in heap all are in RAM 
print(f"identity={id(x)}")  #identity

#COMPARISION OF == AND IS
a=12
b=13
print(a==b)   #check the comparision it give false
print(a is b)  #check the identity of the memory location in heap
a=int(input("enter a number: "))  #enter 254
b=254
print(a is b)   #it give true because of the it act as inter cash mecanism only for IS 
a=int(input("enter a number: ")) #if enter a 1000
b=1000
print(a is b)    #it give false because of that do not know user and compiler
a=257
b=257
print(a is b)
print(f" identity of a: {id(a)},identity of b: {id(b)}")

#OPERATORS
#ARITHMETIC OPERATORS (+,-,*,/,//)
a,b=12,13
print(f"addition: {a+b} ,substraction: {a-b},multiplication: {a*b},division: {a/b}")

#EXPONENT OPERATOR 
print(3**2)   #square
print(3**3)
print(2**4)    #is nothng but two power four =16 only use two star for exponent operator 

print(round(3.56))  
print(round(1.5))

#LOGICAL OPERATOR(AND ,OR,NOT)
a,b,c=25,45,12
print(a>b and b<c or c<b)  #first it check and then go to or
print(not(a<b and b>c or c<b ))

#TERNARY OPERATORS
#it means we write code in one line use if else condition 
a=12
b=45
print("odd number" if (a or b) % 3==0 else "even number")  #ternary operators

#membership operators
name="shruthosha mr "
print("s" in name and "q" in name) #it first check letter and then use boolean 
print("=" *20)
print("THANKYOU")
print("=" * 20)
print("="* 30)
