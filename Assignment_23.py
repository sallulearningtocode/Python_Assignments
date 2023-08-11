# 1. [ print(myiter,end=" ") for myiter in (10,20,30,40,50,60) ]
    
"""2.
def n_Odd(n):
    value = 1
    while value < n:
        yield value
        value += 2

for value in n_Odd((int(input()))*2):
    print(value,end=" ")"""

"""3.
def n_Even(n):
    value = 2
    while n:
        yield value
        value += 2
        n-=1

for value in n_Even((int(input()))):
    print(value,end=" ")"""

"""4.
def n_Square(n):
    value = 1
    while n:
        yield value*value
        value += 1
        n-=1

for value in n_Square((int(input()))):
    print(value,end=" ")"""

"""5.
def n_Square(n):
    a=-1
    b=1
    c = 0
    while n:
        c=a+b
        yield c
        a=b
        b=c
        n-=1

for value in n_Square((int(input()))):
    print(value,end=" ")"""

"""6.
def isPrime(n):
    if n<2:
        return False
    else:
        for j in range(2,int(n**0.5)+1):
            if n%j==0:
                return False
        return True
    
def nPrime(n):
    count=0
    num=2
    while count<n:
        if isPrime(num):
            print(num)
            count+=1
        num+=1

nPrime(10)
"""

"""7.
def my_fib(n):
    a=-1
    b=1
    c=0
    while c<n:
        c=a+b
        yield c
        a=b
        b=c
for value in my_fib(144):
    print(value)"""

"""8.
def primes():
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
        num += 1

prime_generator = primes()

for i in range(100):
    print(next(prime_generator))
"""

"""9.
def greeting_decorator(func):
    def wrapper(s1,s2,s3):
        print("Hello, how are you?")
        if func(s1,s2,s3):
            return s1+s2+s3
    return wrapper

@greeting_decorator
def isvalid(s1,s2,s3):
    if s1<=0 or s2<=0 or s3<=0:
        return False
    elif s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
        return True
    else:
        return False

s1,s2,s3=1,3,3
print(isvalid(s1,s2,s3))"""

def coprime_decorator(func):
    def wrapper(num1,num2):
        if hcf(num1,num2)==1:
            return func(num1,num2)
        else:
            print("The two numbers are not coprime")
    return wrapper

@coprime_decorator
def hcf(num1,num2):
    if num2==0:
        return num1
    else:
        return hcf(num2,num1%num2)

print(hcf(70,7))

# def greetings(func):
#     print('Hello')
#     def wrapper():
#         func()
#         print('Khan')
#     return wrapper

# @greetings
# def salut():
#     print("Mr. Salman ")

# salut()