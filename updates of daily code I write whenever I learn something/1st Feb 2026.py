# Count vowels, consonants, digits in a string

string=list(input())
vowels=0
consonant=0
digits=0
for I in string:
  if I.lower() in "aeiou":
    vowels+=1
  elif I.isalpha() and I.lower() not in "aeiou":
    consonant+=1
  elif I.isdigit():
    digits+=1
  else:
    pass
print(f"vowels in the string are : {vowels}")
print(f"consonants in the string are : {consonant}")
print(f"digits in the string are : {digits}")

# Reverse each word in a sentence (not order)

sentence=input().split()
reverse=[]
for I in sentence:
   I=I[::-1]
   reverse.append(I)
print(" ".join(reverse))

# Check if a list is palindrome
check_list=input().split()
for I in check_list:
  if check_list==check_list[::-1]:
    a="palindrome"
  else:
    a="not palindrome"
print(a) 

# Find third largest number without sort
numbers=list(map(int,input().split()))
                                # a reminder float('-inf') rrepresent smallest no.possible
first=float('-inf')
second=float('-inf')
third=float('-inf')

for I in numbers:
  if I>first:
    first=I
  elif I>second and I!= second:
    second=I
  elif I>third and I!= third:
    third=I 
print(f"third largest number is : {third}")

# Remove duplicates from list but keep order
sentence=input().split()
without_duplicate=[]
for I in sentence:
  if I not in without_duplicate:
    without_duplicate.append(I)
print(" ".join(without_duplicate) )

# Find first non-repeating character in string
string=input().split()
freq={}
for x in string:
  freq[x]=freq.get(x,0)+1
for x in string:
  if freq[x]==1:
   a=x
   break
print(f"the first non repiting word is : {a}") 

# Check if two strings are rotations of each other
string_1=input("type first word : ").strip()
string_2=input("type second word : ").strip()


if len(string_1)==len(string_2):
   temp=string_1+string_1
   if string_2 in temp:
    print("rotation")
   else:
    print("not rotaion")
else:
  print("not rotaion")

# Print frequency of words in paragraph
paragraph=input().lower()
paragraph=paragraph.split()
freq={}
for I in paragraph:
  freq[I]=freq.get(I,0)+1
print(freq)

# Find common elements in two lists without set
l1=input().split()
l2=input().split()

temp=[]

if len(l1)>len(l2):
  for I in range(len(l2)):
    if l2[I] in l1:
      temp.append(l2[I])
  print(temp)
elif len(l2)>len(l1):
  for I in range(len(l1)):
    if l1[I] in l2:
      temp.append(l1[I])
  print(temp)
elif len(l1)==len(l2):
  for I in range(len(l1)):
    if l1[I] in l2:
      temp.append(l1[I])
  print(temp)
else:
  print("no common elements")

# Shift all zeros of list to end without changing order
list_1=input().split()

for I in range(len(list_1)) :
  if list_1[I] == "0" :
    a=list_1.pop(I)
    list_1.append(a)
print(list_1)
