import random

def number(length)->integers:
    numbers=list("1234567890")
    raw_guess=random.sample(numbers,length)
    if raw_guess[0]=="0":
        raw_guess=random.randint(1,9)
    return "".join(raw_guess)