# PRICECON
# cook your dish here
for t in range(int(input())):
    n,k=map(int,input().split())
    m=list(map(int,input().split()))
    loss=[]
    for I in m:
        if I>k:
            loss.append(I-k)
    print(sum(loss))
#CHFCLASS
# cook your dish here
for t in range(int(input())):
    n=int(input())
    weeks=n//7
    if (weeks*7)+6 in range(n+1):
        print(weeks+1)
    else:
        print(weeks)
