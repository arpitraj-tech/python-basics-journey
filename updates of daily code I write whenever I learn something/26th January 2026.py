#taking input in one line from the user and returning the sum

numbers = list (map (float, input().split() ))
print(sum(numbers))
print("\n")
# taking input from the user and returning the max number 

numbers=list (map (float, input().split() ))
print(max(numbers))
print("\n")

#taking input and returning the numbers after multiplication

numbers = list(map(float, input().split()))

product = 1
for num in numbers:
    product *= num

print(product)
print("\n")

#reversing the input by map and list

object = list(map(str,input().split() ))
reverse=object[ : : -1 ]
print (reverse)
print("\n")

#counting how many numbers are even 

numbers = list(map(int,input().split() ))
even=[ ]
for num in numbers :
    if num%2 == 0:
       even.append(num)
       
print(even)
print("\n")

#find second largest number

numbers = list(map(float,input().split() ))
numbers.sort()
print(numbers[-2])
print("\n")

#square every number

numbers = list(map(float,input().split() ))

num=[ ]
for I in numbers :
    square= I*I
    num.append(square)
print(num)    
print("\n")

# remove duplicate no.s

numbers = list(map(int,input().split() ))

singles = [ ]
for num in numbers:
    if num not in singles:
        singles.append(num)
print(singles)        
