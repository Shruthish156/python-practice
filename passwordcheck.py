print("=========PASSWORD CHECKING==========")
while True:
    print("INSTRUCTION")
    print("1. password should contain min 8 character!!")
    print("2. email id must be real and genuine")
    print("3. all are should be valid ")
    
    #take user input
    email_id=input("enetr a person email id: ")
    pass_word=input("enter a person password: ")

    print()

    #check it 
    if len(email_id)>15 and len(pass_word)>=8:
        print(f"the person email id :{email_id} and password :{pass_word} is strong")
    elif len(email_id)>8 and len(pass_word)<8:
        print(f"The person email id :{email_id} and password :{pass_word} is weak")
    else:
        print("the person email id and password is invalid")
    repeat=input("again check the password and email id: (yes/no)")
    if repeat=="no":
        break
