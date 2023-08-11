import random
from threading import Thread
from time import *


""" 1
class arithmetic:
    def multiply(self,a,b,c=1,d=1):
obj1 = arithmetic()
print(obj1.multiply(2,3,4)) """
"""2
    def __init__(self,userid,balance):
        self.userid=userid
        self.balance=balance
    def __add__(self,obj2,obj3):
    
obj1=userAcc(213,80000)
obj3=userAcc(312,98000)
print(obj1.__add__(obj2,obj3))
"""

"""3
    def __init__(self,userid,balance):
        self.userid=userid
        self.balance=balance
    def __str__(self):
obj1=userAcc(213,80000)
obj2=userAcc(333,100000)
print(obj1.__str__())"""


"""4
class even(Thread):
    def run(self):
        for i in range(1,100,2):
            print(i+1)
class odd(Thread):
    def run(self):
        for i in range(0,100,2):
            print(i+1)
obj1=even()
obj2=odd()
obj1.start()
obj2.start()"""

"""5.
class one(Thread):
    def run(self):
        sum=0
        for i in range(0,100,2):
            print(i+1)
            sum=sum+i
        print("Sum is ",sum)
class Two(Thread):
    def run(self):
        sum=0
        for i in range(0,100,2):
            print(i+1)
            sum=sum+i
        print("Sum is ",sum)
obj1=one()
obj2=Two()
obj1.start()
obj2.start()"""

"""6
class one(Thread):
    def run(self):
        list=[]
        for i in range(0,100):
            list.append(random.randint(0,100))
        print(list)
class two(Thread):
        def run(self):
            list=[]
            for i in range(0,100):
                list.append(random.randint(0,100))
            print(list)
class three(Thread):
        def run(self):
            list=[]
            for i in range(0,100):
                list.append(random.randint(0,100))
            print(list)
class four(Thread):
        def run(self):
            list=[]
            for i in range(0,100):
                list.append(random.randint(0,100))
            print(list)

class five(Thread):
        def run(self):
            list=[]
            for i in range(0,100):
                list.append(random.randint(0,100))
            print(list)

obj1=one()
obj2=two()
obj3=three()
obj4=four()
obj5=five()

print("----------First List Items----------")
obj1.run()
print("----------Second List Items----------")
obj2.run()
print("----------Third List Items----------")
obj3.run()
print("----------Fourth List Items----------")
obj4.run()
print("----------Fifth List Items----------")
obj5.run()"""


"""7
class clock(Thread):
    def run(self):
        for i in range(1,120):
            print(time)
            sleep(1)
class minute(Thread):
    def run(self):
        for i in range(0,2):
            print('1 Minute Completed')
            sleep(60)
obj1=clock()
obj2=minute()
obj1.start()
obj2.start()"""

"""8.
class even(Thread):
    def run(self):
        for i in range(1,100,2):
            print(i+1)
class odd(Thread):
    def run(self):
        for i in range(0,100,2):
            print(i+1)
thread=even(name='Your Thread')
thread1=odd(name='My Thread')
obj1=even()
obj2=odd()
obj1.start()
obj2.start()
print(thread.name)
print(thread1.name)"""

"""9
class even(Thread):
    def run(self):
        for i in range(1,100,2):
            print(i+1)
class odd(Thread):
    def run(self):
        for i in range(0,100,2):
            print(i+1)
obj1=even()
obj2=odd()
obj1.start()
obj2.start()
obj1.join()
obj2.join()
print('Bye')"""


"""10
class primechk(Thread):
    def run(self,number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    
class armchk(Thread):
    def run(self,number):
        num_str = str(number)
        num_digits = len(num_str)

        armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

        return armstrong_sum == number

obj1=primechk()
prmchk=obj1.run(17)
if prmchk :
    print("Prime Number")
else:
    obj2=armchk()
    armschk=obj2.run(17)
    if armschk:
        print("Armstrong Number")
    else:
        print("Neither Prime nor Armstrong")"""