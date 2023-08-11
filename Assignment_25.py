"""1.
class profile:
    def __init__(self, name, email, age):
        self.name=name
        self.email=email
        self.age=age
"""

"""2.
class profile:
    def __init__(self, name, email, age):
        self.name=name
        self.email=email
        self.age=age

class updatedProfile(profile):
    def update(self):
        self.name = input("Enter your name: ")
        self.email=input('Enter E-Mail')
        self.age=input('Enter Age')

    def display(self):
        print("Name:",self.name,"E-Mail:",self.email,"Age:",self.age,)
u1=updatedProfile('Salman Khan','khansalman66498@gmail.com',21)
u1.update()
u1.display()"""

"""3.
class profile:
    def __init__(self, name, email, age):
        self.name=name
        self.email=email
        self.age=age
    def display1(self):
        print(self.name,self.email,self.age)


class updatedProfile(profile):
    def update(self):
        self.__name = input("Enter your name: ")
        self.__email=input('Enter E-Mail')

    def display(self):
        print("Name:",self.__name,"E-Mail:",self.__email,"Age:",self.age,)

u1=updatedProfile('Salman Khan','khansalman66498@gmail.com',21)
u1.display1()
u1.update()
u1.display()"""

"""4.
class profile:
    def __init__(self, name, email, age):
        self.name=name
        self.email=email
        self.age=age

class updatedProfile(profile):
    platform=''
    def display(self):
        print("Name:",self.name,"E-Mail:",self.email,"Age:",self.age,'Platform:',self.platform)
    def update(self):
        self.platform=input("Enter platform: ")
u1=updatedProfile('Salman Khan','khansalman66498@gmail.com',21)
u1.update()
u1.display()"""

"""5.
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(a,b):
        return a+b

    def __sub__(a,b):
        return a-b

c1=Calculator(10,20)
print(c1.__add__())
print(c1.__sub__())"""

"""6.
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self):
        return self.a+self.b

    def __sub__(self):
        return self.a-self.b
class smartCalc(Calculator):
    
    def __mul__(self):
        return self.a*self.b
    
    def __div__(self):
        return self.a//self.b
    
c1=smartCalc(20,10)
print(c1.__add__())"""

"""7.
class Phone:
    def sms(slef):
        print('I can be used to send SMS')
    def call(self):
        print('I can be used to make phone calls')
p=Phone()
p.call()
p.sms()"""

"""8.
class Calculator:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b

    def __add__(self):
        return self.a+self.b

    def __sub__(self):
        return self.a-self.b
class smartCalc(Calculator):
    
    def __mul__(self):
        return self.a*self.b
    
    def __div__(self):
        return self.a//self.b

class Phone:
    def sms(self):
        print('I can be used to send SMS')
    def call(self):
        print('I can be used to make phone calls')

class Smartphone(Phone,smartCalc):
    def features():
        print('I am a Smartphone')"""

"""9.
class phonebook:
    def __init__(self):
        self.users={}

class truecaller(phonebook):
        def inputDetails(self):
            name=input('Enter Name')
            number=input('Enter Number')
            self.users[name]=number

        def fetch(self,number):
            for name,phone in self.users.items():
                if phone ==number:
                     print(f'{name} has the phone number {phone}')
                     break
                else:
                     print(f'No user found with the phone number {number}')

p1=truecaller()
p2=truecaller()
p1.inputDetails()
p2.inputDetails()
p1.fetch('4444')
p2.fetch('5555')"""

"""10.
class phonebook:
    def __init__(self):
        self.users={}

class truecaller(phonebook):
        def inputDetails(self):
            name=input('Enter Name')
            number=input('Enter Number')
            self.users[name]=number

        def fetch(self,number):
            for name,phone in self.users.items():
                if phone ==number:
                     print(f'{name} has the phone number {phone}')
                     break
                else:
                     print(f'No user found with the phone number {number}')

class SmartPhone(truecaller):
     def method1(p1):
        p1.fetch('4444')

p1=SmartPhone()
p1.inputDetails()
p1.method1()"""