import random

def guess(x):
    comp_num = random.randint(1,15)
    if x==comp_num:
        return 'You guessed it! Bravo!'
    else:
        return 'Try again!'