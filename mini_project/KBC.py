                             # MAKING A PROGRAM FOR REPLICATING KBC(KON BANEGA CROREPATI)

# greeting the user and telling the rules of the game

print("WELCOME TO KBC".center(130))
print("\nI Arpit Raj welcome u to this platform of KBC\nwhere u have a chance to become a millionaire by answering some questions")
print("\nRULES FOR THE GAME:")
print("\n1.\tu can't take hints from other there is no lifeline  ")
print("2.\tafter each question u will earn a certain amount of money in your dashboard")
print("3.\tafter each question when money is added u will be asked to continue or quit.\n4.\tif u choose quit the amount u win will be yours virtually ofc but,\n5.\tif u choose continue u will be move to the next question and,\n6\tif your answer is correct then this money will be added to ypur previous one and,\n7.\tif incorrect then you loose all the money and game will be closed\n\n")

# Asking for user interest

yes_no=input("so are you ready for the game reply 'yes'or'no' : ")

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

# responding to the yes or no and making dashboard

if yes_no.lower()=="yes":
  print("\n")
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

else:
  print("\nok losers can't make money anyway\t:)\thave a nice future\t:)\t ")
