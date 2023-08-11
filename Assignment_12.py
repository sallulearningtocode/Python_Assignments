# 1
"""a=int(input())
r=0
while a!=0:
    r=r*10+a%10
    a=a//10
print(r)"""

# 2
"""a=int(input())
for i in range(2,int(a/2)+1):
    if(a%i==0):
        print("Non-Prime Number")
        break
else:
    print("Prime Number")"""

# 3
"""print(1,2,3,end=' ')
for i in range(4,101):
    for s in range(2,(i//2)+1):
        if(i%s==0):
            break
    else:
        print(i,end=' ')"""


# 4
"""start=int(input())
end=int(input())
for i in range(start,end+1):
        for s in range(2,i):

            if(i%s==0):
                break
        else:
            print(i,end=' ')"""

# 5
"""a=int(input())
while 1:
  count=0;
  a=a+1
  for i in range(2,a//2):
    if(a%i==0):
        count=count+1
        break
  if count==0:
    print(a)
    break"""

"""6
from math import sqrt
 
# To take input from the user and initialize the variables
num = int(input("Enter a number: "))
count = 0
n = 2
 
print("First", num, "prime numbers are: ")
while count < num:
    # define a flag variable
    prime_flag = True
     
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i) == 0:
            prime_flag = False
            break
     
    # check if flag is True
    if prime_flag:
        print(n, end =" ")
        count = count + 1
    n = n + 1"""


"""7.
a=int(input())
b=int(input())
flag=1
for i in range(2,a):
    if a%i==0:
        flag=0
        break
if flag:
    for j in range(2,b):
        if b%j==0:
            flag=0
            break
    if flag:
        print("Co-Prime Numbers")"""

"""8.
a=0
b=1
c=a+b
n=int(input())
while n:
    print(c)
    a=b
    b=c
    c=a+b
    n=n-1
"""

"""9.
a=int(input())
b=int(input())
max =  a if a>b else b
lcm=0
for i in range(2,max):
    if a%i==0 and b%i==0:
        lcm=i
print(lcm)"""

"""10.
a=int(input())
b=int(input())
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print(a)"""

