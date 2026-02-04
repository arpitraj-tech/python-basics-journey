# find second smallest number without sort:
smallest1=float('inf')
smallest2=float('inf')
numbers=list(map(int,input().split()))
for I in numbers:
  if I<smallest1:
    smallest2=smallest1
    smallest1=I
  elif I < smallest2 and I != smallest1:
    smallest2=I
print(smallest2) 

#counting vowels consonants and digits in a string
string=input()
vowels=0
consonants=0
digits=0
for I in string:
  if I.isalpha():
    if I.lower() in "aeiou":
      vowels+=1
    else:
      consonants+=1
  elif I.isdigit():
    digits+=1
print(f"no. of vowels = {vowels}")
print(f"no. of consonants = {consonants}")
print(f"no. of digits = {digits}")

#merge 2 list without duplicaes
list1 = list(map(str,input().split()))
list2 = list(map(str,input().split()))
temp=[]
for I in list1:
  if I not in temp:
    temp.append(I)
for I in list2:
  if I not in temp:
    temp.append(I)
print(temp)

#check if list is palindrome :
check_list=list(map(str,input().split()))
if check_list==check_list[::-1]:
  print("it's a palindrome")
else:
  print("not a palindrome")

#frequency of words in a paragraph
para=input().lower()
para1=para.split()
freq={}
for I in para1:
  freq[I]=freq.get(I,0)+1
print(freq)

