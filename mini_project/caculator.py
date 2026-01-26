def calculator_manual(num1="1",operator="+",num2="1"):
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
   return value-1
  except:
    print("please write only numbers")





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
   return value
  except:
    print("write only a number")

