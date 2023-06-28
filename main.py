import random

def computer_number():
    return random.randint(1,15)

def guess(x):
    comp_num = computer_number()
    if x==comp_num:
        return 'You guessed it! Bravo!'
    else:
        return 'Try again!'