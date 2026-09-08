#SIMPLE CALCULATOR PROJECT

while True:
    #ask user input of num1
    num1=int(input("enter a first number: "))
    #ask user input of num2
    num2=int(input("enter a second number: "))

    print("1.ADDITION")
    print("2.SUBSTRACTION")
    print("3.MULTIPLICATION")
    print("4.division")
    print("5.EXPONENTIAL")

    #SELECT THE OPERATION
    choose=int(input("choose the number operation(1,2,3,4,5) :"))
    #use match commands
    match choose:
        case choose if choose==1:
            print(f"ADDITION :{num1+num2}")
        case choose if choose==2:
            print(f"SUBSTRACTION :{num1-num2}")
        case choose if choose==3:
            print(f"MULTIPLICATION :{num1*num2}")
        case choose if choose==4:
            print(f"DIVISION : {num1/num2}")
        case choose if choose==5:
            print(f"EXPONENTIAL : {num1**num2}")
        case _:
            print("invalid operation :")
    again=input("can you again do calculation(yes,no):")
    if again=="no":
        break          #it will stop the program 
    



