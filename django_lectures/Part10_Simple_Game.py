###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
# import random
# print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")
# digits = list(range(10))
# random.shuffle(digits)
# random_digits = digits[:3]
# print("Code has been generated, please guess a 3 digit number.")
# print(random_digits)
#
# # Another hint:
# guess = input("What is your guess? ")
# # print(type(guess))
#
# # Think about how you will compare the input to the random number, what format
# # should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
#
# def check_match(num):
#     # convert guess into a list for comparison
#     input_digits = [int(char) for char in str(num)]
#     for i in range[3]:
#         if random_digit
#
#     return
#
# print(check_match(guess))
import random

# GET GUESS
def get_guess():

    return list(str(input("What is your guess")))

# GENERATE COMPUTER CODE 123
def generate_code():

    digits = [str(num) for num in range(10)]

    # shuffle the input_digits
    random.shuffle(digits)

    #then grab the first 3 digits
    return digits[:3]

# GENERATE THE CLUES
def generate_clues(code, user_guess):

    # first check if the user's guess matches the CODE
    # if so, we are done and that's all we had to do
    if user_guess == code:

        return "CODE CRACKED!"

    clues = []

    for ind, num in enumerate(user_guess):
        # must check for a match before checking if it's close
        if num == code[ind]:

            clues.append("Match")

        elif num in code:

            clues.append("Close")

    if clues == []:
        return ["Nope"]
    else:
        return clues

# RUN GAME LOGIC
print("Welcome Code Breaker!")

secrect_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED!":

    guess = get_guess()

    clue_report = generate_clues(guess, secrect_code)

    print("Here is the result of your guess: ")

    for clue in clue_report:

        print(clue)
