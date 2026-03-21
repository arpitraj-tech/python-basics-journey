import random

def password_generator(level):
    char=list("qwertyuiopasdfghjklzxcvbnm")
    charu=list("QWERTYUIOPLKJHGFDSAZXCVBNM")
    sym=list("!@#$%&")
    num=list("1234567890")
    
    if level=="easy":
        charecters=random.sample(char,6)
        upper=random.sample(charu,2)
        raw_password=charecters+upper
        arranged=random.shuffle(raw_password)
        return "".join(raw_password)

    if level=="medium":
        charecters=random.sample(char,3)
        numbers=random.sample(num,3)
        upper=random.sample(charu,2)
        raw_password=charecters+numbers+upper
        arranged=random.shuffle(raw_password)
        return "".join(raw_password)

    if level=="hard":
        charecters=random.sample(char,3)
        numbers=random.sample(num,3)
        upper=random.sample(charu,3)
        symbols=random.sample(sym,3)
        raw_password=charecters+numbers+upper+symbols
        arranged=random.shuffle(raw_password)
        return "".join(raw_password)

