#Difficulty:Easy
#what is the point? choose your adventure
#################################################
score=0
username=input('Hello,Hello To your adventure could you type in your name champ:')
print(f"Alright {username},Here we go!")

answer=input('You are on a foggy path you dont know which way to go! would you wanna go right or left?').lower()

if answer=='right':
    print("You made the right choice now you found a torch!")
    score+=1
    answer=input("You have seen a house from far and a chest near you will you reach for the chest or go to the house? \n type chest or house : ").lower()
    if answer =='house':
        score+=1
        print("You made the right choice,you v'seen a fridge will you open it or not!")
    elif answer=='chest':
        score-=100
        print(f"You made a bad desicion there is plenty of snakes inside and snake bites you now you ll die! \n You lost dumbass! Score = {score}")  
elif answer == 'left':
    print("Your way will get darker and darker!")
    score -=1
    answer= input("you see to ways suddenly you remebred when your grandfather in his deathbed when he told to always go to straight to the point so will you go the point or let your grandfather down and go left again? type straight or left : ")
    if answer == 'straight':
        print("Good choice ! You are in Narnia \n You won")
        score+=99
        print(score)
    elif answer == 'left':
        score-=99
        print("You lost ")
        print(score)

   
else:
    print("Please type in right or left nothing else!")



