from chatterbot import ChatBot
import os

# the calculator AI will not learn with the user input
Bot = ChatBot(name='Calculator',
              read_only=True,
              logic_adapters=["chatterbot.logic.MathematicalEvaluation"],
              storage_adapter="chatterbot.storage.SQLStorageAdapter")


# clear the screen and start
os.system('cls' if os.name == 'nt' else 'clear')
print("Hello, I am a calculator. How may I help you?")
while (True):

    user_input = input("me: ")

    
    if user_input.lower() == 'quit':
        print("Exiting")
        break

    # print invalid input if the AI is unable to comprehend the input
    try:
        response = Bot.get_response(user_input)
        print("Calculator:", response)
    except:
        print("Calculator: Please enter valid input.")
