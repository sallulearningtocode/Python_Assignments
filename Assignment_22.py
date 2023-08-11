"""1.
def sumN(n):
    if n>0:
        return n+sumN(n-1)
    else:
        return 0

print(sumN(10))"""

"""2.
def sumN(n):
    if n>0:
        return n*2-1+sumN(n-1)
    else:
        return 0

print(sumN(10))"""

"""3.
def sumN(n):
    if n>0:
        return n*2+sumN(n-1)
    else:
        return 0

print(sumN(10))"""

"""4.
def sumN(n):
    if n>0:
        return n**2+sumN(n-1)
    else:
        return 0

print(sumN(10))"""

"""5.
def sumN(n):
    if n>0:
        return n**3+sumN(n-1)
    else:
        return 0

print(sumN(10))"""

"""6.
def sumN(n):
    if n!=0:
        return n*sumN(n-1)
    else:
        return 1

print(sumN(5))"""

"""7.
def sumN(n):
    if n!=0:
        return n%10+sumN(n//10)
    else:
        return 0

print(sumN(321744))"""

"""8.
def bin(n):
    if n>0:
        print(n%2)
        bin(n//2)
    else:
        return
bin(64)"""
        
"""9.
def oct(n):
    if n>0:
        oct(n//8)
        print(n%8)
    else:
        return
oct(69)"""

"""10.
def nFib(n):
    if n<=2:
        return n-1
    else:
        return nFib(n-1)+nFib(n-2)
print(nFib(8))"""