import random

"""1.
def ret(l1):
    l2=l1
    return l2
l1=[10,20,30,40,50,60]
l2=ret(l1)
print(l2)"""

"""2.
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(isprime(11))"""

"""3.
def printEven(l1):
    for i in l1:
        if i%2==0:
            print(i)
l1=[1,2,3,4,5,6,7,8,9]
printEven(l1)"""

"""4.
def ispalin(s1):
    str=""
    for i in s1:
        str=i+str
    if str==s1:
        print("Palindrome")
    else:
        print("Not a Palindrome")

s1="nitin"
ispalin(s1)"""

"""5.
def min3(l1):
    return min(l1)
l1=[510,20,30]
print(min3(l1))"""

"""6.
num=[(i*2) for i in range(1,31)]
print(num)"""

"""7.
def increment(l1):
    return l1+1
def doubleincrement(l1):
    return increment(l1)+1
l1=7658
print(doubleincrement(l1))"""

"""8.
def pangram(sen):
    test="abcdefghijklmnopqrstuvwxyz"
    flag=1
    for i in test:
        if(sen.find(i)<0):
            flag=0 
    if flag:
        return "It's an anagram"
    else:
        return "It's not an anagram"

sen='quick brown fox jumps over the lazy dog'
print(pangram(sen))"""

"""9.
def pangaram(sen):
    test="abcdefghijklmnopqrstuvwxyz"
    print(len(sen))
    for x in range(len(test)):
        if test[x] not in sen:
            return 0
    return 1

sen="The Quick Brown Fox Jumps Over A Lazy Dog".lower()
print(pangaram(sen))"""

"""10
def anagram(first,second):
    for x in second:
        if x not in first:
            return 0
    return 1

first="saman"
second="almans"
print(anagram(first,second))
"""