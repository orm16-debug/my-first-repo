input random
VALID_OPTIONS = ["rock", "paper", "scissors"]

# ASK USER FOR AN INPUT (R/P/S)

user_choice = input("Please choose one of 'rock', 'paper', or 'scissors': ")
print("User: ", user_choice)

# VALIDATIONS

if user_choice not in VALID_OPTIONS:
    print("Please input valid choice")
    quit()

# GENERATE RANDOM COMPUTER CHOICE

computer_choice = random.choice(VALID_OPTIONS)
print("Comp: ", computer_choice)

# DETERMINE THE WINNER