'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([0, 1, -1])
print(computer)

youstr=input("Enter your choice:")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"snake",-1:"water",0:"gun"}
you=youDict[youstr]
print(f"Computer chose:{reverseDict[computer]}")
print(f"You chose:{reverseDict[you]}")
if (computer==you):
    print("It's a Draw")
else:    
    if(computer==-1 and you==1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You Lose!")
    elif(computer==1 and you==0):
        print("You Win!")  
    elif(computer==1 and you==-1):
        print("You Lose!")      
    elif(computer==0 and you==1):
        print("You Lose!")    
    elif(computer==0 and you==-1):
        print("You Win!")
    else:
        print("Something went wrong")    
