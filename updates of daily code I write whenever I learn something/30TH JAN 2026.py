# cook your dish here
#P4HOME
for I in range(int(input())):
    x,y,z=map(int,input().split())
    chef=x
    friends=list(range(x-y,x+y+1))
    allowed=list(range(x-z,x+z+1))
    if chef in friends:
      if chef in allowed:
        if len(allowed)>len(friends):
          print(len(friends)-1)
        elif allowed==0:
          print(0) 
        else:
         print(len(allowed)-1 )

# cook your dish here
#      FARFROMO
for I in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    def distance(x,y):
        import math
        return math.sqrt(x**2+y**2)
    if distance(x1,y1)>distance(x2,y2):
        print("alex")
    elif distance(x2,y2)>distance(x1,y1):
        print("bob")
    else:
        print("equal")

# cook your dish here
#      RCTGLD
for I in range(int(input())):
    n=int(input())
    if n<4:
        print(0)
    elif n%4==0:
        print(int((n/4)*(n/4)))
    elif n%4!=0:
        if n%4==3 or n%4==2:
            print(int(((n//4)+1)*(n//4)))
        if n%4==1:
            print(int(((n-1)/4)*((n-1)/4)))  

# cook your dish here
#    WORDLE
for w in range(int(input())):
    s=list(input())
    t=list(input())
    a=[]
    for char in range(len(s)):
        if s[char] == t[char]:
         a.append("g")
        elif s[char] != t[char] :
            a.append("b")
            
    print("".join(a))    
    
