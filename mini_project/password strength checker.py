# password strength checker
print("Password strength checker".center(120))
password=list(input("\n\ntype your password : ") )
print("\n")
count=0
if len(password)>=8:
  count+=0.5
if len(password)>10:
  count+=0.8

if any(I.isupper() for I in password) :
  count+=0.6
if any(I.islower() for I in password):
  count+=0.6
if any(I.isdigit() for I in password) :
  count+=1
if any(I in "!@#$%^&*" for I in password):
  count+=1
if any(I.isspace() for I in password[1:-1]):
  count+=0.5

if count<=2:
  print("Your password is weak")
elif count<=4:
  print("your password strength is moderate")
else:
  print("your password strength is strong")
