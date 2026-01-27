# remove duplicates using set 

num=set(map(int,input().split()))
print(num)
print("\n")

# count frequency using dictionary

num=list(map(int,input().split()))
freq={}
for I in num :
  frequency=num.count(I)
  freq[I]=frequency
print(freq)
print("\n")

#tupple unpacking and give sum
tup=tuple(map(int,input().split()))
print(tup)
a=list(tup)
print(sum(a)) 
print("\n")

# ccommon elements of 2 lists using set

list_1=list(map(int,input().split()))
list_2=list(map(int,input().split()))

a=set(list_1) 
b=set(list_2)

print(a.intersection(b))
print("\n")

#creating dictionary from two lists 

names=list(map(str,input().split()))
age=list(map(int,input().split()))

dictionary={}

for I in range(len(names)):
  dictionary[names[I]]=age[I]

print(dictionary)
print("\n")

#highest frequency element 


num=list(map(int,input().split()))
freq={}
for I in num :
  frequency=num.count(I)
  freq[I]=frequency
print(max(freq,key=freq.get))
print("\n")

#solved two sum problem on leet code (1st problem)

class Solution:  # ddon't know class function and self yet it was already written there I wrote from seen
    def twoSum(self, nums: List[int], target: int) -> List[int]: # tthis was also  written already
        seen={}
        for I in range(len(nums)):
            need=target-nums[I]

            if need in seen:
                return [seen[need],I ]
            seen[nums[I]]=I


# solved 13 question on CodeChef also 10 dificultby level less than 165 1 400 and 1 200
