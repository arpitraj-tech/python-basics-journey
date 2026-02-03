# making sign up and login system and then after logging assigning some task which user can do
#this was made with mobile on Google colab 
#(simple version now no screen refresh or text color or sound or images or anything as making it through mobile and Google colab not in vs code or pycharm so after I get my laptop after 2 or 3 months then I will remake this with all features and more advance like in kbc in mini project it just the same question one with no lifeline etc I am adding that here only but later it will give random 7 question from the set of many question which will make it more interesting every time u play and post it to the project file on git hub but for now I will post this on the mini project section not the project)
"""Ask user:

   1st ask for sign up
   if password weak then ask for creating password again
   then ask for login or create new account
   if login then type valid username and password
   if create new account then type new username and password (atores the previous as well u csn use now both to login)


   Stores valid username and passwords in dictionary.
   Check login.

   then ask for what u now want to do play kbc, use simple calculator or want to analyze a sentence

   """

def password_strength(password):
  count=0
  if len(password)>=8:
    count+=0.5

  if any(I.isupper() for I in password) :
    count+=0.7
  if any(I.islower() for I in password):
    count+=0.7
  if any(I.isdigit() for I in password) :
    count+=1
  if any(I in "!@#$%^&*" for I in password):
    count+=1
  if any(I.isspace() for I in password[1:-1]):
    count+=0.5

  return count

def kbc(ready):
  print("WELCOME TO KBC".center(120))
  print("\nI Arpit Raj welcome u to this platform of KBC\nwhere u have a chance to become a millionaire by answering some questions")
  print("\nRULES FOR THE GAME:")
  print("\n1.\tu can't take hints from other there is no lifeline  ")
  print("2.\tafter each question u will earn a certain amount of money in your dashboard")
  print("3.\tafter each question when money is added u will be asked to continue or quit.\n4.\tif u choose quit the amount u win will be yours virtually ofc but,\n5.\tif u choose continue u will be move to the next question and,\n6\tif your answer is correct then this money will be added to ypur previous one and,\n7.\tif incorrect then you loose all the money and game will be closed\n\n")

  # making list for prizes

  prizes=[10_000,
          50_000,
          1_00_000,
          10_00_000,
          25_00_000,
          50_00_000,
          1_00_00_000,
          7_00_00_000]


  # making the list of questions to be asked

  questions=["\nso your 1st question is :\n\nIn which year India got independence\n",
            "\nso your 2nd question is:\n\nin which year Russia Ukraine war strarted\n",
            "\nso your 3rd question is:\n\nbetween 2025 to 2026 in which country does America has attacked whats the reason\n",
            "\nso your 4th question is:\n\nwhich is the highest civilian award an Indian can get\n",
            "\nso your 5th question is:\n\nin which year covid-19 started to spread\n",
            "\nso your 6th question is:\n\nwho wrote the sacred history of Mahabharat\n",
            "\nso your 7th question is:\n\nwho is the 1st wife of lord krishna\n",
            "\nso your final question for seven crore rupees is:\n\nwho is the life of lord krishna\n"
            ]

  # making list of options

  options=["A: 1965   B: 1975   C: 1978   D: 1974",
           "A: 2021   B: 2020   C: 2023   D: 2022",
           "A: Russia  B: Greenland,  C: Iran  D: venenjula",
           "A: Bharat ratna  B: padma bhusan  C: padma shree D: bharat chakra",
           "A: 2022  B: 2021  C: 2020  D: 2019 ",
           "A: ved yas  B: valmiki  C: lord ganesh  D: lord krishna",
           "A: Shri Radha  B: Rukmini  C: satyabhama  D: jambawati",
           "A: Shri Radha  B: Rukmini  C: satyabhama  D: jambawati"
           ]

  # making the list of solutions of the above questions

  answers=["B",
           "A",
           "D",
           "A",
           "D",
           "C",
           "A",
           "A",
           ]




  print("\n\n")
  print("ok let's the game begin\n".center(120))
  dashboard=0
  print(f"winning amount = ₹{dashboard}".center(220))
  print("\nyour winning amount will be visible in the right corner of the screen")
  print("\n")

  #now using loops for starting the game and question to become visible

  for question in range(0,len(questions)):
    print(questions[question])
    print(options[question])
    print("\n")
    answer=input("enter your answer : ")
    if answer.upper()==answers[question]:
      print(f"\n\t\t\t\tcongratulations for winning ₹{prizes[question]} \n")
      dashboard=dashboard+prizes[question]
      print(f"winning amount = ₹{dashboard}".center(220))
      print("\n")
      continue_quit=input("do you want to continue or quit for continue press 1 and for quit press 0 : ")
      if continue_quit=="0":
        print("\n\n\n\n")
        print(f"CONGRATULATIONS FOR WINNING ₹{dashboard}, THIS AMOUNT WILL BE CREDITED TO U VIRTUALLY,  THANKS FOR PLAYING".center(150) )
        break
      else:
        print("\n\n\n")
      if question==7 :
        print("\n\n\n\nCONGRATULATIONS FOR WINNING THE KBC GAME ".center(200) )
        break
    else:
      print("\n\nOPS!!!  wrong answer u lost all your money :) ".center(130))
      break
  return "redirecting to previous page"

def calculator_user(num1=(), operator=(), num2=() ):
  num1=input("enter 1st number : ")
  operator=input("what operator you want to use '+','-','*','/' : ")
  num2=input("enter 2nd number : ")
  try:
   match operator:
     case "+":
      if float(num1) and float(num2):
        value=float(float(num1)+float(num2))
      else:
       value=int(int(num1)+int(num2))
     case "-":
      if float(num1) and float(num2):
        value=float(float(num1)-float(num2))
      else:
       value=int(int(num1)-int(num2))
     case "*":
      if float(num1) and float(num2):
        value=float(float(num1)*float(num2))
      else:
       value=int(int(num1)*int(num2))
     case "/":
       if num2==0:
         value=("can't devide by zero")
       else:
        if float(num1) and float(num2):
         value=float(float(num1)/float(num2))
        else:
         value=int(int(num1)/int(num2))
  except:
    print("write only a number")
  return f"the value of {num1}{operator}{num2} is {value}"
  return "\n\nredirecting to previous page"

def analyze_sentence():
  print("Sentence analyzer\n\n".center(140))

  sentence=input("type your sentence : ").split()

  #for no. of words
  print("\n no. of words in the sentence are : ", len(sentence))

  #for no. of charecters
  char="".join(sentence)
  print("\n no. oof charecters in the sentence is : " , len(char))

  #for longest word
  print("\n the longest word in the sentence is : ", max(sentence,key=len))

  #for shortest word
  print("\n the shortest word in the sentence is : ", min(sentence,key=len))

  #for frequency of each word
  freq={}
  for x in sentence:
    freq[x]=freq.get(x,0)+1
  print(f"\n frequency of words are as follows : {freq}")

  #sentence reversed (in word order) like India is beautiful -> beautiful is India # nnot like lufitueab ...... aas for this u can simply use [::-1] in simple sting case not with list
  reverse=" ".join(sentence[::-1])
  print(f"\n sentence in reverse order is : {reverse}")

  return "redirecting to previous page"

def code_decode():
  ask=input("do u want to code a secret text or decode : ").strip()
  if ask.lower() == "code":
      code_txt=input("type the msg u want to be coded  : ").lower()
      coding_structure = str.maketrans( { "a":"14h", "e":"67j","i":"12s","o":"10r","u":"1n1","b":"56u","c":"3m3", "d":"7o8","f":"101b","g":"615","h":"8oo","j":"oo2","k":"00o","l":"14oo7","m":"qw10","n":"881q","p":"1b","q":"occ","r":"69x","s":"5o0","t":"jj1","v":"1no","w":"1xs","x":"1se0","y":"004n","z":"3kk0","0":"!!!@#","1":"@%","2":")*","3":"_&","4":"%(","5":"^^","6":"*$","7":"$^","8":"&%@","9":"###" } )
      coded_output= code_txt.translate(coding_structure)
      print(coded_output)
      print("now share the secret with whomever u wish ; )")
  elif ask.lower() == "decode":
      code_txtr=input("type the msg u want to be decoded  : ").lower()
      reverse_structure = { "14h":"a", "67j":"e","12s":"i","10r":"o","1n1":"u","56u":"b","3m3":"c","7o8":"d","101b":"f","615":"g","8oo":"h","oo2":"j","00o":"k","14oo7":"l","qw10":"m","881q":"n","1b":"p","occ":"q","69x":"r","5o0":"s","jj1":"t","1no":"v","1xs":"w","1se0":"x","004n":"y","3kk0":"z","!!!@#":"0","@%":"1",")*":"2","_&":"3","%(":"4","^^":"5","*$":"6","$^":"7","&%@":"8","###":"9" }
      decoded_output = code_txtr
      sorted_keys = sorted(reverse_structure.keys(), key=len, reverse=True)

      for coded_charecter, original_charecter in reverse_structure.items():
          decoded_output = decoded_output.replace(coded_charecter, original_charecter)

      print(decoded_output)
      print("this is the msg someone send u ; ) ")
  return "redirecting to previous page"








print("Sign_Up/Login".center(120))
print("\n\n")

sign_up={}

ask_username=input("Please create user name for sign up : ")
print("\n")
ask_password=input("Please create password for sign up : ")
print("\n")
check=password_strength(ask_password)

while check<=2:
  check=password_strength(ask_password)
  print("password is very weak plss make a strong password\n")
  ask_password=input("Please create password for sign up : ")

  print("\n")
  if check>2:
    break
sign_up.update({ask_username:ask_password})
print("\n")

ask_choice=input("If u want to create new account, type( 1 ) or if login, type ( 2 ) : ")
print("\n")
while ask_choice=="1":
  ask_username=input("Please create user name for sign up : ")
  while ask_username in sign_up.keys():
      print("\nusername already in use please try another\n")
      ask_username=input("Please create user name for sign up : ")
  print("\n")
  ask_password=input("Please create password for sign up : ")
  print("\n")
  check=password_strength(ask_password)
  ask_choice=input("If u want to create new account, type( 1 ) or if login, type ( 2 ) : ")

  while check<=2:
    check=password_strength(ask_password)
    print("password is very weak plss make a strong password\n")
    ask_password=input("Please create password for sign up : ")

    print("\n")
    if check>2:
      break
  sign_up.update({ask_username:ask_password})

print("\n")

if ask_choice=="2":
  while True :
    ask_username=input("Please type your user name for login : ")
    print("\n")
    while ask_username not in sign_up.keys():
      print("username not found")
      print("\n")
      ask=input("if u forgot your username type (1) to exit, if want to retry type anything like letter no.(except 1 )or press enter ")
      if ask=="1":
        exit()
        break
      else:
        ask_username=input("\nPlease type correct user name for login : ")
      if ask_username in sign_up.keys():
        print("\n")
        break
    ask_password=input("Please enter password for log in : ")
    print("\n")
    while ask_password!=sign_up[ask_username]:
      print("password is incorrect")
      print("\n")
      ask_p=input("if u forgot your password type (1) to exit if want to retry type (2) or enter and if u want to login another I'd type (3)")
      if ask_p=="1":
        exit()
        break
      if ask_p=="3":
        break
      else :
        ask_password=input("\nPlease enter correct password for log in : ")
    if ask_password==sign_up[ask_username]:
      break
    continue
print("\n")
print("login successful")
print("\n\n")

while True:

  print("what u want to do now".center(120))
  print("\n")
  print("option 1 : play kbc game\noption 2 : use simple calculator\noption 3 : analyze a sentence\noption 4 : code or decode a secret text\noption 5 : log out\noption 6 : do nothing ")
  print("\n")
  ask_option=input("type your option : ")
  print("\n")

  if ask_option=="5":
    print(" sucessfully log out".center(120))
    exit()
    break

  elif ask_option=="6":
    print("u have selected to do nothing ")
    cc=input("if u wish any time just type 1 or else u type anything except 1 u will be logged out")
    if cc=="1":
     continue
    else:
     print(" sucessfully log out".center(120))
     exit()
     break
  while True :

    if ask_option=="1":
      print("\n")
      while True :
        asking=input("whenever u are ready just type 'ready' :").lower()

        if asking =="ready":
          break
        else:
          print("please only type ready ")
          continue
      kbc("ready")
      break
    if ask_option=="2":
      print("simple calculator".center(120))
      print("\n")
      print(calculator_user())
      break
    if ask_option=="3":
      print("\n")
      analyze_sentence()
      break
    if ask_option=="4":
      print("code or decode a secret text".center(120))
      print("\n")
      code_decode()
      break
    else:
      print("wrong option")
      break
