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
