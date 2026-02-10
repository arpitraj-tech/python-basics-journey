from data import * 

def add_contact():
    while True:    
      name=input("\nplease enter the name u want to save as : ").lower()
      while name in user_contacts.keys():
          asking=input("user already exist u can either press '1' for updating the phone no. of user or press '2' for new contact for new name : ")
          while asking not in ["1","2"]:
              asking=input("u can either press '1' for updating the phone no. of user or press '2' for new contact for new name : ")
          if asking == "1":
              break
          if asking == "2":
              name=input("\nplease enter the name u want to save as : ").lower()
      
      print("\n")
      phone=input("please enter the phone no. without +91 and spaces between numbers : ").strip()
      
      while not phone.isdigit() or len(phone) != 10 :
           print("\nplease enter the correct no. and without spaces\n") 
           phone=input("please enter the phone no. without +91 and spaces between numbers : ").strip()
      
      phone_num=f"+91{phone}"
      user_contacts[name]=phone_num
      print("\nthe number is successfully saved")
      break
      
def search():
      search_for=input("Enter the name : ").lower()
      if search_for not in user_contacts.keys() :
         return("\ncontact not found\n")
      else:  
         return (user_contacts[search_for]) 
      
      
def delete():
    delete_contact=input("Enter the name which u want to delete : ")           
    if delete_contact not in user_contacts.keys():
        print("user not found")
    else:
      del user_contacts[delete_contact]
      print(f"contact deleted successfully")
    
def show():
        for key,value in user_contacts.items():
            print(f"{key} : {value}\n")

