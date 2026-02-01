# password strength checker
print("Password strength checker".center(120))
password=list(input("\n\ntype your password : ") )
print("\n")
count=0
if len(password)>=8:
  count+=0.39
else:
  count=0

for I in password:
  if I.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    count+=0.12
  if I.isupper() :
    count+=0.80
  if I.islower():
    count+=0.19
  if I.isdigit():
    count+=0.49
  if I in "!@#$%^&*":
    count+=0.70
  if I.isspace():
    count+=0.71

if count<1.5:
  print("Your password is very weak")
elif count<=3:
  print("your password is weak")
elif count<5.5:
  print("your password strength is moderate")
elif count<=7.3:
  print("your password strength is strong")
else:
  print("your password strength is very strong")  
