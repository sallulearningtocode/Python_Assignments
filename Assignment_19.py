"""1.
def printm():
    print("MYSIRG")
printm()"""

"""2.
def printxy(x,y):
    print(x,y)
printxy(10,20)"""

"""3.
def sumn(*args):
    return sum(args)
print(sumn(2,3,4,5))"""

"""4.
def sumn(**kwargs):
    sum=0
    for args in kwargs.values():
        sum+=int(args)
    return sum
total_marks=sumn(Maths=98,English=96,PC=98,DS=98,Python=97)
print("Percentage is ",(total_marks/500)*100)"""

"""5.
def suml(a):
    return sum(a) 
print(suml([1,2,3,4,5]))"""

"""6.
def MaxOfFour(a,b,c,d):
    if a>b and a>c and a>d:
        return a
    elif b>c and b>d:
        return b
    elif c>d:
        return c
    else:
        return d
gretest=MaxOfFour(1,2,3,4)
print(gretest)"""

"""7.
def sumn(l1):
    return sum(l1)
l1=[10,20,30]
print(sumn(l1))"""

"""8.
def sumn(l1):
    m=1
    for i in l1:
        m=m*i
    return m
l1=[10,20,30]
print(sumn(l1))
"""

"""9.
def a(num,start,end):

    if num in range(start,end):
        print(1)
    else:
        print(0)

a(11,start=2,end=20)"""

"""10.
def find(n):
    if n%2==0:
        print('Even')
    else:
        print('Odd')
find(21)"""