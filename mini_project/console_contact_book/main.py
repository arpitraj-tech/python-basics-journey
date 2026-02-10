from contacts import * 
from data import *

print("Welcome to contact book".center(130))
print("\n\n")

while True :
    ask=input("please chose from the options below : \n1.Add contacts\n2.search contact by name\n3.delete contact by name\n4.show all contacts\n5.exit()\n\n")
    print("\n")
    while ask not in ["1","2","3","4","5"]:
        ask=input("please chose from the options below : \n1.Add contacts\n2.search contact by name\n3.delete contact by name\n4.show all contacts\n5.exit()\n\n")
        print("\n")
        
    if ask=="1":
        add_contact()
        print("\n")
    
    if ask =="2":
        print(search())
        print("\n")
        
    if ask =="3":
        print("\n")
        delete()     
        
    if ask =="4":
        show()
    
    if ask =="5":
        break
