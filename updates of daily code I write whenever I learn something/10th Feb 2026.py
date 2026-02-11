# cook your dish here
'''FLOWERBUY'''
for t in range(int(input())):
    n=int(input())

    print((n//3)*5) if n%3==0 else print((n//3)*5+4) if n%3==2 else print((((n//3)-1)*5)+8)

# cook your dish here
'''NOTIME'''
n,h,x=map(int,input().split())
num=list(map(int,input().split()))
count=None
if h<=x:
   print("yes")
else:
    for y in num:
        if (y+x)>=h:
          count=1
    if count==None:
        print("no")
    elif count==1:
        print("yes")

# cook your dish here
'''FIRSTANDLAST'''
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    maximum=a[0]+a[n-1]
    for x in range(n-1):
        current=a[x]+a[x+1]
        if current>maximum:
            maximum=current
    print(maximum)
    
# cook your dish here

'''DISCOOKIE''' 
for t in range(int(input())):
    n, m = map(int, input().split())

    if m < n:
        sec = n - m
    else:
        remainder = m % n
        sec = min(remainder, n - remainder)

    print(sec)

'''self practice'''

#remove duplicates using set but keep order

a=list(map(str,input().split()))
b=set(a)
c=[]
for x in a :
  if x in b:
    b.remove(x)
    c.append(x)
print(c)

# intersection of 2 lists

list_1=set(list(map(str,input().split())))
list_2=set(list(map(str,input().split()))) 
intersection_list=list_1&list_2
print(intersection_list)

# first non repeating charecte without dictionary as in with dictionary u can unpack key and value by.item and then ask if value=1 break and print it's key

string=list(map(str,input().split()))
non=[]
for x in string:
  non.append(x)
  string.remove(x)
  if x not in string:
    break
  elif x in string:
    non.remove(x)
print(non)


# rotate list by k

list_1= list(map(str,input().split()))
k=int(input()) 
reverse=k%len(list_1)
print(list_1[reverse::]+list_1[:reverse])

# check anagram using dict not counter

string_1=input().strip()
string_2=input().strip()
string_3=list(string_1)
string_4=list(string_2)
freq={}
freq_2={}
isanagram=False
for x in string_3:
  freq[x]=freq.get(x,0)+1
for x in string_4:
  freq_2[x]=freq_2.get(x,0)+1
for key,value in freq.items():
  if key not in freq_2.keys():
    isanagram=False
    break
  if key in freq_2.keys():
    if freq_2[key]==value:
      isanagram=True
  
print("they are anagram") if isanagram==True else print("they are not anagram")


