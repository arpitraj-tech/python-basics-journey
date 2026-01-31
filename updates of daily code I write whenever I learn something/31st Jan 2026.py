# Count frequency of characters in a string using dictionary
string=input()
freq={}
for I in string:
  freq[I]=freq.get(I,0)+1
print(freq)

# Reverse order of words in a sentence
string=input().split()
reverse=string[::-1]
"".join(reverse)
print(reverse)

# Find second largest number in list without sort
numbers=list(map(int,input().split()))
largest=float('-inf')
second_largest=float('-inf')
for I in numbers:
  if I>largest:
    largest=I
  elif I>second_largest and I!=largest:
    second_largest=I
print(f"the largest value is : {largest}")
print(f"the second largest no. is : {second_largest}") 

# Check if two strings are anagrams
x,y= map(str,input().split())
list(x)
list(y)

for I in range(len(x)):
  if len(x)==len(y):
    if x[I] not in y:
      count="not anagram"
      break
    count="anagram"
print(count)    

# Remove duplicates from list without using set
sentence=list(map(str,input().split()))
temp=[]
for I in range(len(sentence)):
  if sentence[I] not in temp:
    temp.append(sentence[I])
non_duplicate_sentence=" ".join(temp)
str(non_duplicate_sentence)
print(non_duplicate_sentence)  
  
