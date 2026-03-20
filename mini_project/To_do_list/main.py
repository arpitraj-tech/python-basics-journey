import functions as fs 
import os 
import time
def clear():
    if os.name=="nt":
        os.system('cls')
    else:
        os.system('clear')


while True:
    print("welcome to to do list".center(120))
    print("1. add task\n2. update task\n3. delete task\n4. show tasks\n5. Exit")

    ask=input("Please type the option (1,2,3,4,5) to proceed ")
    while ask not in "12345":
        ask=input=("Please type the option (1,2,3,4,5) to proceed ")
    if ask=="1":
        fs.add_task()
        time.sleep(2)
        clear()
    elif ask=="2":
        fs.update_task()
        time.sleep(2)
        clear()
    elif ask=="3":
        fs.delete_task()
        time.sleep(2)
        clear()
    elif ask=="4":
        fs.show_task()
        time.sleep(5)
    elif ask=="5":
        print("exit success")
        exit()
        break
