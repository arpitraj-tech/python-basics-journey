
# cook your dish here
'''LONGDRIVE'''
"""SOLUTION By ME"""
for t in range(int(input())):
    x,y=map(int,input().split())
    distance=x*10
      
    for I in range(1,10000):
      if x==y or x>y:
        print(0)
      else:
          temp=distance+100
          new=(temp)//(10+I)
          distance=temp
          if new>=y:
           print(I)
           break
            
# cook your dish here
'''LONGDRIVE'''
"""SOLUTION BY SOMEONEELSE"""  """LESS TIME COMPLEXITY AND SIMPLE"""
import math
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        print(0)
    else:
        c=math.ceil((10*(b-a))/(100-b))
        print(c)

'''EXPLAINED BY GOOGLE'''
"""
Think of it as finding the tipping point where your extra driving outweighs your slow start.
To reach a higher average speed Y, every new hour you drive at 100 km/h contributes "bonus" speed that fills the "gap" 
left by your initial slower hours.
Step-by-Step Logic
 * Find the Distance Gap: In your first 10 hours, you were Y - X km/h slower than your goal every hour.
   This means you are "behind" by a total of 10 \times (Y - X) kilometers.
 * Calculate Hourly Gain: When you drive at 100 km/h, but your target is Y,
   you are gaining 100 - Y kilometers of "surplus" distance toward your goal every hour.
 * Divide to Solve: To find how many hours (c) you need, divide the total "gap" by your "hourly gain."

C=10(y-x)/100-y
   
Why the Formula is Better
 * No Guessing: Unlike a loop that checks 1, 2, or 3 hours, the formula gives the answer instantly.
 * Precision: Using math.ceil ensures that if you need 4.2 hours to hit the target, the code rounds up to 5,
   because you can only count full hours in this problem.
Advice for Beginners: Don't worry if the algebra feels heavy. Practice converting "word problems" into balance equations (Distance In = Distance Needed), and the math will start to feel like a shortcut rather than a hurdle.
"""  
