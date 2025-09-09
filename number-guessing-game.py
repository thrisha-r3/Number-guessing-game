from random import randint

hard_n=5
easy_n=10

def check_the_number(guess,answer):
    if guess<answer:
        return 'Too low'
    if guess>answer:
        return 'Too high'
    else:
        return 'correct answer'

def set_diff():
    while True:
        level=input("Enter the difficulty either type 'easy' or 'difficult'").strip().lower()
        if level=='easy':
            return easy_n
        elif level=='difficult':
            return hard_n
        else:
            print("Invalid input1 please tye 'easy' or 'difficult")


print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 100")
answer=randint(1,100)
guess=0
turns = set_diff()
print(f"you have {turns} attempts to guess the number")
while guess!=answer and turns!=0:

    guess=int(input("Make a guess"))
    print(check_the_number(guess,answer))
    turns-=1
    if guess!=answer:
        print(f"you have {turns} attempts to guess the number")

