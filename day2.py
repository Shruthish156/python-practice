#IF ELSE CONDITIONs 
while True:
    name=input("enter a boy name : ")
    age=20
    if name=="sumanth" and age>=18:
        print("he is eligeble for voting!!")
    elif age<18:
        print("not eligeble!!")
    elif age>18:
        pass                   #it is use when we have not specific  logic .it run successfully but not print output
    else:
        print("invalid!") 

    repeat=input("again enter the user name(yes/no)")
    if repeat=="no":
        break

#IN PYTHON NOT USE SWITCH STATEMENT COMPARE TO C,JS,CPP ONLY USE MATCH COMMANDA IT WORK AS SWITCH TYPE BUT DIFFER UPDATE
age=int(input("enter a age: "))
match age:
    case age if age%2==0:
        print("good person!!")
    case age if age==3:
        print("good businessman")
    case _:
        print("invalid")
person=input("enter a male person name:")
match person:
    case "ramaaiah" | "summu":
        print("name is correct:")
    case "raju":
        print("invalid name:")
    case _:
        print("invalid")
    

