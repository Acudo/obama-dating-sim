# Modules
import time

# Definitions
def name():
    n = input("First of all, what is your name? ")
    yn = input(f"{n}, is that correct? (y/n) ")
    if yn == 'y':
        print(f"Hopyfully your name will become {n} Obama, haha")
    elif yn == 'n':
        name()
    else:
        print("I don't quite understand. I'll assume it's a yes")
    return n

# The Game

# Start
print("Welcome to the Obama Dating Simulator")

# Asking for name
name = name()
