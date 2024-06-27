# Difficulty: Easy
# The Goal: Whenever the user gives the right answer, we add a point to their score

q_bank = {"Does Messi have 8 Ballon d'Ors?": False, "Is CR7 the GOAT?": True}

score = 0

while True:
    initial = input("Welcome, User!\nAre you ready to start the quiz?\nIf you want to start, type 'Y'. Otherwise, type 'N': ").strip().upper()
    
    if initial == 'Y':
        print("Here we go!")
        
        # Quiz logic starts here
        for question, answer in q_bank.items():
            user_answer = input(f"{question} (True/False): ").strip().capitalize()
            if user_answer == str(answer):
                score += 1
                print("Correct!")
            else:
                print("Incorrect.")
        
        # Print the final score
        print(f"Your final score is: {score}")
        break  # Exit the loop after the quiz is finished

    elif initial == 'N':
        print("We won't miss you.")
        quit()  # Exit the program
    else:
        print("Please enter one of the given values: 'Y' or 'N'.")

print(f"This is you Score : {score}")
