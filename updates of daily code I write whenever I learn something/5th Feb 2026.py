#finding second largest in a list
num=list(map(int,input().split()))
first=float('-inf')
second=float('-inf')
for I in num:
    if I>first:
        second=first
        first=I
    elif I>second and I !=first:
       second=I
print(second)

# remove duplicate from a list without set
list_= list(map(str,input().split()))
list_1=[]
for I in range(len(list_)):
    if list_[I] not in list_1:
        list_1.append(list_[I])
print(list_1)

# count frequency of charecters
string1=input().lower()
string=list(string1.split())
freq={}
for x in string:
    freq[x]=freq.get(x,0)+1
print(freq)

#reverse words in sentence
sentence=list(map(str,input().split()))
sentence_reverse=sentence[::-1]
print(" ".join(sentence_reverse))

#check anagram
import collections
word1,word2=map(str,input().split())
print("is anagram") if collections.Counter(word1)==collections.Counter(word2) else print("not anagram")    

#checking if palindrome 
word=input().strip()
print("is palindrome") if word==word[::-1] else print("not a palindrome")

#merge two list without duplicates
list_1=list(map(str,input().split()))
list_2=list(map(str,input().split()))
list_3=[]
for x in range(len(list_1)):
    if list_1[x] not in list_3:
        list_3.append(list_1[x])
for x in range(len(list_2)):
    if list_2[x] not in list_3:
        list_3.append(list_2[x])
print(list_3)

#count vowels consonants and digits
string=list(input())
vowels=0
consonants=0
digits=0
for x in string:
    if x.isalpha():
       if x in "aeiou":
         vowels+=1
       else :
         consonants+=1
    if x.isdigit():
        digits+=1
print(f"no. of vowels is : {vowels}\nno.of consonants is : {consonants}\nno. of digits is : {digits}")

# find missing no. in 1.....n list
num=list(map(int,input().split()))
a=[]
for x in range(1,num[-1]):
    if x not in num:
        a.append(x)
print(a)

# short dictionaries by values
d={"a":2,"b":4,"c":1,"d":7}                                                                 #taken help from Google as not know lamda yet                                  
sorted_d = dict(sorted(d.items(),key=lambda item: item[1]))       #d.items() -> gives [("a",2),("b",4).....]
print(sorted_d)                                                                                        # key=lambda item : item[1]  -> sort using value and dict convert back to dictionary
#checking if 2 strings are rotation pf each other
string1=input().strip()
string2=input().strip()
if len(string1)==len(string2):
    if string2 in string1+string1:
        print("it's rotation of each other")
    else:
        print("not rotation")
else:
    print("not rotation")
    
#flattened nested list              done by me 
list1=["1","2","3","4",["5","6","7","8","9","10"]]
list2=[]
for x in list1:
    for y in x:
        list2.append(y)
print(list2) 
#flattened done by Google (searched after doing all)
flat = [y for x in list1 for y in x]
