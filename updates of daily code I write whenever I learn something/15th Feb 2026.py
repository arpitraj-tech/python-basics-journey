# cook your dish here
'''TWOVSTEN'''
for t in range(int(input())):  
    x=int(input()) 
    count=0  
    if x%10 == 0:     
        print(0)    
    elif x%10 != 0 and x%5 == 0 :   
        while True:
            a = x*2
            count+=1 
            if a%10 == 0:
                break       
        print(count)        
    else :
        print(-1)

# cook your dish here
'''CARRANGE'''
for t in range(int(input())):
    p,m,v = map(int,input().split())
    if p > 1 :
        milage_decrease = p-1
        new_milage = m-milage_decrease
        print(v*new_milage)
    else:
        print(m*v)  
