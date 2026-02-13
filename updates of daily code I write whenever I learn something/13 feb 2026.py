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
