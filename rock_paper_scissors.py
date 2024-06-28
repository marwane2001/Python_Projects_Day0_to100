import random

options = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

while True:
    user_input = input('Could you please type Rock/Paper/Scissors or Q to quit: ').lower()
    if user_input == 'q':
        print(f"Final Scores:\nYou: {user_score}\nComputer: {computer_score}")
        break
    if user_input not in options:
        print("Invalid input, please try again.")
        continue
    
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f"Computer picked: {computer_pick}.")
    
    if user_input == 'rock' and computer_pick == 'scissors':
        user_score += 1
        print("You won!")
    elif user_input == 'paper' and computer_pick == 'rock':
        user_score += 1
        print("You won!")
    elif user_input == 'scissors' and computer_pick == 'paper':
        user_score += 1
        print("You won!")
    elif user_input == computer_pick:
        print("It's a draw!")
    else:
        computer_score += 1
        print("You lost!")

print("Thanks for playing!")
