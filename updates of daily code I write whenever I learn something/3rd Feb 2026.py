"""
all solved by me on code chef (no help taken like yeasterday)
and also today I not done gpt questions as I was busy in a mini project which I completed today and I will upload it today only in reposetry
"""
## DRUNKALK ##  
# cook your dish here
for I in range(int(input())):
    count=0
    k=int(input())
    for x in range(1,k+1):
        if x%2!=0:
            count+=3
        else:
            count-=1
    print(count)

## LAYERCAKE ##
# cook your dish here
for t in range(int(input())):
    a,b=map(int,input().split())
    n=list(map(int,input().split()))
    m=list(map(int,input().split()))
    count=0
    for I in m:
        for x in n:
            if I<x :
                count+=1
    print(count)

#rest was very easy (1 to 5 lines no loop just basic and in one I learn about math.ceil()
