import function as f 

level=input("Plese tell the level of password u wanna generate easy medium hard : ").lower().strip()
expected="easymediumhard"

while True:
    if level not in expected:
        print("please type easy medium or hard")
        level=input("Plese tell the level of password u wanna generate easy medium hard : ").lower().strip()
        print(f"Your Generated password is : {f.password_generator(level)}")
        break


