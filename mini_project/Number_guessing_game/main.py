import functions as f 

length=int(input("please enter the length of digits you want to guess : ").strip())
if length==0:
    exit()

a=int(f.number(length))
count=0
while True :
        num=int(input("please enter your no. : ").strip())

        if num<a:
            count+=1
            print("ops! your no. is smaller please retry ")

        elif num>a:
            count+=1
            print("ops! your number is greater please retry")
        elif num==a:
            count+=1 
            print(f"hurray!! your guess was correct in '{count}' turns")
            break
        
