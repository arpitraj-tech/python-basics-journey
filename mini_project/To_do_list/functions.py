import json,os

with open("data.json","r") as f :
    datas=json.load(f)

def save_data():
    with open("data.json","w") as file :
        json.dump(datas,file,indent=4)

def add_task():
    count=0
    x=input("please enter the task u wanna add : ")
    while True:
        if count>=3:
            print("task addition failed plss retry ")
            print( f"Task failed to be added")
            break
        a=input("tell wheter task is done or not done : ").lower().strip()
        if a=="done":
            datas["task_history"].append([{x:"status = Done"}])
            save_data()
            print( f"task {x} updated succesfully")
            break
        elif a=="not done" or a=="notdone":
            datas["task_history"].append([{x:"status = Not done"}])
            save_data()
            print( f"task {x} updated succesfully")
            break
        else:
            print("please only enter done, not done or notdone charecter case dosen`t matter")
            count+=1

def delete_task():
    count=0
    try:
        while True:
            try:
                if count>=3:
                    break
                x=int(input("for checking serial no. u can display all the task by show list then note the no. \nenter the serial no. of the task u want to delete or press enter 3 times to exit this phase :").strip())
                break
            except:
                print("enter only a integer")
                count+=1
        del datas["task_history"][x-1]
        save_data()
        print( f"task {x} successfully deleted")
    except:
        Error

def show_task():
    try:
        for index,value in enumerate(datas["task_history"]):
            for keys,values in datas["task_history"][index][0].items():
                a=keys
                b=values
            print(f"{index+1} - task-> {a} : status-> {b}")
    except:
        Error

def update_task():
    try:
        while True:
            try:
                count=0
                x=int(input("for checking serial no. u can display all the task by show list then note the no. \nenter the serial no. of the task u want to upddate :").strip())
                while True:
                    if count>=3:
                        print("task updation failed plss retry with valid inputs")
                        break
                    y=input("task is done or not done : ").lower().strip()
                    if y=="done" or y=="notdone" or y=="not done":
                        break
                    else:
                        print("please enter only done,notdone,not done and charecter case not matters")
                        count+=1
                break
            except:
                print("enter only a integer")
        key=list(datas["task_history"][x-1][0].keys())
        valid_key=key[0]
        datas["task_history"][x-1][0][valid_key]=y.title()
        save_data()
        print( f"task {x} successfully updated")
    except:
        Error




