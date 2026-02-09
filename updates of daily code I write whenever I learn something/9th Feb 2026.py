# cook your dish here
''' NOWINNER'''
for t in range(int(input())):
    a,b,c,m=map(int,input().split())
    x1=abs(b-a)
    x2=abs(c-a)
    x3=abs(c-b)
    print("yes") if x1<=m or x2<=m or x3<=m else print("no")

# find duplicates in a list without nested loops:
dup_list = list(map(str, input("Enter elements separated by spaces: ").split()))

freq = {}
for x in dup_list:
  freq[x] = freq.get(x, 0) + 1

duplicates = []
for x, count in freq.items():
  if count > 1:
    duplicates.append(x)

print(duplicates)

# check if two lists have common elements :
list_1=list(map(str,input().split()))
list_2=list(map(str,input().split()))
I=[]
for x in list_1 :
  if x in list_2:
    I.append("yes")
  else:
    I.append("no")
if "yes" in I:
  print("it has common elements")
else:
  print("no it not has any common elements")

#remove duplicates while keeping order
list_1=list(map(str,input().split()))
non_list=[]
for I in list_1:
  if I not in non_list:
    non_list.append(I)
print(non_list)

#count frequency of elements using dict
string=list(map(str,input().split()))
freq={}
for x in string:
  freq[x]=freq.get(x,0)+1
print(freq)

# find first non repeating elements 
string=list(map(str,input().split()))
a=len(string)
for x in range(len(string)):
  if string[x] not in string[x+1:]:
   print(string[x])
   break

# reverse a list without slicing 
list_1=list(map(str,input().split()))
nr=[]
for x in range(len(list_1) - 1, -1, -1):
  nr.append(list_1[x]) 
print(nr)

# rotate list by kth position 
list_1=list(map(str,input().split()))
k=int(input())
r=k%len(list_1)
print(list_1[r:]+list_1[:r])

#check if list is palindrome
list_1=list(map(str,input().split()))
print("its a palindrome") if list_1 == list_1[::-1] else print("not a palindrome")
