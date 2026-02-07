'''
Difficulty:940
##  COJPRESSVD  ##
Learn problem solving techniques required to solve this problem
Take our problem solving courses to understand how to attempt problems like these.
Start Learning
Compress the Video
Chef recorded a video explaining his favorite recipe. However, the size of the video is too large to upload on the internet. He wants to compress the video so that it has the minimum 
(1≤i≤N) such that the value of the 
ith frame is equal to the value of either of its neighbors and remove the ithframe.
Find the minimum number of frames Chef can achieve.

Input Format
First line will .......
  - the values of the frames.
Output Format
For each test case, output in a single line the minimum number of frames Chef can achieve.

4
1
5                 1
2
1 1               1
3
1 2 3             3
4
2 1 2 2           3
'''

# cook your dish here
''' DONE BY ME ONLY '''
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x=a.copy()
    x.append(0)
    x.insert(0,0)
    b=[]
    for I in range (1,len(a)+1):
      if x[I]!=x[I+1]:
         b.append(x[I])

    print(len(b))

'''
Difficulty:940
Make Subarray

You want the black cells to form a contiguous subarray, 
 Note that if there are no black cells, this condition is satisfied.
You can only change the colour of a cell from white to black (but not the other way around). Find the minimum number of changes needed.

Input Format
The first line of input will contain a single integer 
T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains 
N - the number of cells.
The second line contains 
S - a binary string of size n
Output Format
For each test case, output on a new line the minimum number of cells that need to be changed from white to black, such that the black cells form a contiguous subarray.
'''
# cook your dish here
'''MAKESUB'''
for I in range(int(input())):
    n=input()
    s=input()
    first=s.find("1")
    last=s.rfind("1")
    a=s[first:last+1].count("0")
    print(a)

'''
Am I Lucky!
A school has organized a field trip for a class of 
N
N students, of which 
X students are boys, and the remaining students are girls.
Everyone is excited to go trekking, and must form groups of size exactly 

K to do so. However, boys will only form groups among themselves, and girls will only form groups among themselves.
Both boys and girls will form as many groups as possible.

The remaining students can either dance around a bonfire, or just read books.
Dancing around the bonfire requires a pair of one girl and one boy, while reading is done alone.

Reading is much more boring than dancing, so students will try to avoid it.
What's the minimum number of students who will be engaged in reading?
'''
# cook your dish here
'''SPCP4'''  '''TRIED TO SOLVE IN A EXPLAINING WAY'''
for I in range(int(input())):
    n,x,k=map(int,input().split())
    boys=x
    girls=n-x
    boys_grp=boys//k
    boys_remain=boys-(boys_grp*k)
    girls_grp=girls//k 
    girls_remain=girls-(girls_grp*k)
    read=abs(boys_remain-girls_remain)
    print(read)

