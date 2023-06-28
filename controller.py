import random

computer_number = random.randint(1, 15)


def guess(x):
    comp_num = computer_number
    if x == comp_num:
        return "You guessed it! Bravo!"
    elif x<comp_num:
        return "It is higher!"
    else:
        return "It is lower!"
