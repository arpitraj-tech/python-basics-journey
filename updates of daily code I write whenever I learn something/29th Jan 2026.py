#taking numbers and printing squares
numbers=list(map(int,input().split()))
print( [ x*x for x in numbers ] )

#taking numbers and printing only odd numbers 
numbers=list(map(int,input().split()))
print( [ x for x in numbers if x%2!=0 ] )

#taking teo list and making dictionary using list 
list_1=list(map(int,input().split()))
list_2=list(map(int,input().split()))
print( dict ( zip ( list_1 , list_2 ) ) )

#Take numbers → make dictionary {number: square}
numbers=list(map(int,input().split()))
print ( dict ( zip ( numbers , [ x*x for x in numbers ] ) ) )

#Take sentence → make list of words
msg=list(map(str,input().split()))
print(msg)

#count frequency of numbers using .get()
numbers=list(map(int,input().split()))
freq={ }
for I in numbers:
    freq[I]=freq.get(I,0)+1
print (freq)    

# cook your dish here ############     ALJMP ###############
t=int(input())
for I in range(t):
    n=int(input())
    if n%2!=0: #odd
       print(int((n//2)+1))
    else :
        print(int(n/2))
        
# frog jumps n-1 like if on 6th position it will jump 5 times means think it like 
# if frog  is  initially at 5 means right most corner then it will jump left most then 
#again right but it can't jump to the same position twice 
#so 1st it was on 6th then 1 then 5 then 2 then 4 then 3 and now all is filled so last position is 3 
