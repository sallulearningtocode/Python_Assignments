"""1
a=10
b=0
c=a/b"""

"""2
a=10
b=int(input())
c=a/b"""

"""3
a=10
b=0
try:
    c=a/b
except Exception as e:
    print(e)"""

"""4
a=10
try:
    b=int(input())
    c=a/b
except ValueError as e:
    print("There has been a Value Error")
print(c)"""


"""5
try:
    a=int(input())
    b=int(input())
    c=a/b
    if a==b:
        raise ArithmeticError()
    print(c) 
except TypeError:
    print('Operands must have same type')
except ValueError:
    print('Please inpput numbers only')
except ZeroDivisionError:
    print("Don't input 0 as number")
except ArithmeticError:
    print("DOn't use the same number as it always gives 1")"""

"""6
try:
    a=int(input())
    b=int(input())
    if a==b:
        raise ArithmeticError()
    choice = int(input('Press 1 to Add these numbers\nPress 2 to find Difference\nPress 3 to Find Product\nPress 4 to find quotient'))
    match choice:
        case 1:
            print(a+b)
        case 2:
            print(abs(a-b))
        case 3:
            print(a*b)
        case 4:
            if b!=0:
                print(a/b)
            else:
                raise ZeroDivisionError()
except TypeError :
    print("Operands must be numbers only")
except ZeroDivisionError:
    print("There Shouldn't be zero as operand")
except ValueError:
    print("There's been a Value Error")
except ArithmeticError:
    print("Numbers can't be same")"""

"""7
try:
    a=int(input())
    b=int(input())
    if a==b:
        raise ArithmeticError()
    choice = int(input('Press 1 to Add these numbers\nPress 2 to find Difference\nPress 3 to Find Product\nPress 4 to find quotient'))
    match choice:
        case 1:
            print(a+b)
        case 2:
            print(abs(a-b))
        case 3:
            print(a*b)
        case 4:
            if b!=0:
                print(a/b)
            else:
                raise ZeroDivisionError()
except TypeError :
    print("Operands must be numbers only")
except ZeroDivisionError:
    print("There Shouldn't be zero as operand")
except ValueError:
    print("There's been a Value Error")
except ArithmeticError:
    print("Numbers can't be same")

finally:
    print('Happy Calculating')"""


"""8
a=int(input())
b=int(input())
try:
    c=a/b
    if b!=0:
        print(c)
    else: 
        raise ZeroDivisionError()
    
except ZeroDivisionError:
    print("Operands can't be zero")
else:
    print("Wan't to do more operations?")"""

"""9
try:
    a=input()
    b=input()
    if isinstance(a,int) and isinstance(b,int):
        print(a*b)
    else:
        raise ValueError()
except ValueError:
    print("Please Use Numbers as Operands")"""

"""10
try:
    a=int(input())
    b=int(input())
    if isinstance(a,int) and isinstance(b,int):
        try:
            c=a/b
        except ZeroDivisionError:
            print("You can't Divide a number by 0")
        else:
            print(a/b)
    else:
        raise ValueError()
except ValueError:
    print("Please Use Numbers as operands")"""
