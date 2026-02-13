# cook your dish here
'''MINDAYSRET'''
"""Tried to solve by modules for improvement in time complexity(just started learning)"""
import sys
import math
for t in range(int(sys.stdin.readline())):
    n,k=map(int,sys.stdin.readline().split())
    print(math.ceil(n/k))

# cook your dish here
'''WCC'''
'''Don't know why readline doesn't work here I guess I need improvement here'''
for t in range(int(input())):
    x=int(input())
    result=input().lower()
    #total_prize=100*x#no use
    #c is victory by carison
    #n is victory by chef
    #d is draw
    a=result.count("c")
    b=result.count("n")
    c=result.count("d")
    print(60*x) if a>b else print(55*x) if a==b else print(40*x)

# cook your dish here
'''CEILRCPT'''
"""IMPORTANT"""
for t in range(int(input())):
    p = int(input())

    x = (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048)
    m = list(x)

    m.sort(reverse=True) #it's important so that largest no. iis considered first as minimum is required 

    count = 0
    remaining = p #set variable name

    for x in m:
        if remaining == 0:
            break
        else:
          count += remaining//x    #it tells how many of this no. iis used to make it
          remaining %= x     #it again go to loop by changing the remaining variable value it's like using recursion 

    print(count)
