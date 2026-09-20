while True:
    import random 
    #it will take any random number from 1 to 50
    num=random.randint(1,50)      
    #ask the user for input
    guess=int(input("enter a number from(1-50):"))
    #check the guess number
    if guess>=1 and guess<=50:     #it will check number. if true enter loop
        if guess>num:
            print(f"the guessing number of accuracy is high my number is :{num}")
        elif guess<num:
            print(f"the guessing number of accuracy is low my number is :{num}")
        elif guess==num:
            print(f"the guess number is 100% correct my number is :{num}")
    else:
        print("you entered number is invalid and out of range(1-50):")
    repeat_enternum=input("again check the number:(yes/no)")
    if repeat_enternum=="no":
        break