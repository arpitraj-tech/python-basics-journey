'''done by me only'''
# cook your dish here
'''SAMESAME'''

for t in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(str,input().strip()))
    b=list(map(str,input().strip()))
    
    if len(a)==len(b):
     count=0
     for x in range(m):
        if b[x] != a[x]:
            count+=1
     print(count)
  
    else:
        count=0
        temp=[]
        while len(a)>m:
            for x in range(m):
                if b[x] != a[x] :
                    count+=1
            temp.append(count)
            count=0
            a.remove(a[0])
        count=0
        for x in range(m):
            if b[x] != a[x] :
             count+=1
        temp.append(count)
            
        print(min(temp))

# cook your dish here
'''DRAWCH'''
for _ in range(int(input())):
    n,m=map(int,input().split())
    s=input()
    a=s.count("1")
    b=s.count("0")
    c=abs(a-b)
    d=(n-m)-c
    if d == 0:
        print("Yes")
    elif d<0:
        print("No")
    else:
        if d%2 == 0:
            print("Yes")
        else :
            print("No")

# cook your dish here
'''CABRIDE'''
for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(200)
    elif n%2 == 0 :
        a=n//2
        print(a*200)
    else:
        a=n//2 
        print((a*200)+100)

# cook your dish here
'''BELOW 2 ARE DONE BY ME'''

''' this is the correct code'''
import sys
input=sys.stdin.readline
for _ in range(int(input().strip())):
    n = int(input().strip())
    if n>0:
      small_coins = [n // 2, n // 3, n // 4]
      total_small = sum(small_coins)
      print(max(n, total_small))
    else :
        print(0)

''' this is also correct''' 

for _ in range(int(input())):
    n = int(input())
    if n>0:
      small_coins = [n // 2, n // 3, n // 4]
      total_small = sum(small_coins)
      print(max(n, total_small))
    else :
        print(0)

### but due to error in this platform maybe here it's not working


# cook your dish here
'''copied from other common submission which is used by ALL OTHERS'''
def exchange_coin(n, memo={}):
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    exchange_value = exchange_coin(n//2) + exchange_coin(n//3) + exchange_coin(n//4)
    memo[n] = max(n, exchange_value)
    return memo[n]

while True:
    try:
        n = int(input())
        print(exchange_coin(n))
    except EOFError:
        break
#cook your dish here
'''MXON'''

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    ones = s.count('1')
    if ones == 0 or k == 0:
        print(ones)
        continue
    last_one = s.rfind('1')
    zeros_left = s[:last_one].count('0')
    result = ones + min(k, zeros_left)
    print(result)

# cook your dish here
'''JMARKET'''
import sys
inputx=sys.stdin.readline

for t in range (int(inputx().strip())):
    
    x,a,b,c = map(int,input().split())
    
    lis=[a,b,c]
    lis.sort()
    
    n=x-1
    m=1 
    
    print((n*lis[0])+(m*lis[1]))

#cook your dish here
'''TEKKEN'''
for _ in range(int(input())):
    a,b,c = map(int, input().split())
    d = abs(b-c)
    if a > d:
        print("YES")
    else:
        print("NO")
