#Difficulty:Easy
#what is the point? let the user guess the random number
#################################################
import random

score = 0
target_score = 2  

while True:
    r = random.randrange(0, 10)
    answer = input("Guess the value (between 0 and 9): ")
    
    try:
        if int(answer) == r:
            print('Good answer')
            score += 1
            if score == target_score:
                print(f"Congratulations! You've reached the target score of {score}.")
                break
        else:
            print(f"Wrong! The correct answer was {r}. Try Again!")
    except ValueError:
        print("Please enter a valid number.")

print(f"Your final score is: {score}")
