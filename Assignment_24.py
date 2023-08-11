"""1.
class user:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
"""

"""2.
class user:
    def __init__(self):
        print("WELCOME")

u1=user()"""

"""3.
class user:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    def display(self):
        print("Name : ",self.name,"Age = ",self.age,"Email = ",self.email,sep='  ')
u1=user('abc',21,'abc@gmail.com')
u2=user('def',22,'def@gmail.com')
u1.display()
u2.display()"""

"""4.
class user:
    def __init__(self,name='',age=0,email=''):
        self.name=name
        self.age=age
        self.email=email
    def display(self):
        print("Name : ",self.name,"Age = ",self.age,"Email = ",self.email,sep='  ')
u1=user()
u2=user('Khan',20,'khansalman')
u1.display()
u2.display()"""

"""5.
class user:
    def __init__(self,name='',age=10):
        self.name=name
        self.age=age
    def __del__(self):
        del self.age
        print('Age is Deleted')
u1=user('alan',20)
print(u1.name,u1.age)
"""

"""6.
class user:
    def __init__(self,name,age,):
        self.name=name
        self.age=age
    def youngestOfAll(self,u2,u3):
        if self.age<u2.age:
            print(self.name,'is Youngest of All')
        elif u2.age<u3.age:
            print(u2.name,'is Youngest of All')
        else:
            print(u3.name,'is Youngest of All')

u1=user('alan',21)
u2=user('man',20)
u3=user('nea',34)
u1.youngestOfAll(u2,u3)"""

"""7.
class laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd

    def showConfig(self):
        print(self.brand,self.cpu,self.hdd,self.ram)

l1=laptop('Macbook Pro',8,'M1 MAX',512)
l1.showConfig()"""

"""8.
class laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd

    def showConfig(self):
        print(self.brand,self.cpu,self.hdd,self.ram)

def key(e):
    return e.ram

L1=[
    laptop('hp',8,'intel',512),
    laptop('lenovo',4,'intel',1),
    laptop('dell',16,'intel',512)]

L1.sort(key=key)

for i in L1:
    i.showConfig()"""

"""9.
class School:
    city_name = 'New Delhi'
    def __init__(self,name):
        self.name=name

s1=School('Raj Modern')
s2=School('Gagan Public School')
s3=School('Goverdhan Modern Public Schhol')

print(s1.name,s1.city_name)"""

"""10.
class Employee:

    def __init__(self,name='',empid=0,salary=0):
        self.empid=empid
        self.name=name
        self.salary=salary

    def input(self):
        self.name=input('Enter Name ')
        self.empid=int(input('Enter Employee Id '))
        self.salary=int(input('Enter Salary '))

    def display(self):
        print(self.name,self.empid,self.salary,sep=' ')

e1=Employee('Salman',3221,50000)
e2=Employee()
e3=Employee()
e2.input()
e3.input()
e1.display()
e2.display()
e3.display()"""