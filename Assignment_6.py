#1.PYTHON SCRIPT TO CHECK WHETHER A GIVEN NUMBER IS POSITIVE OR NON-POSITIVE
"""f=int(input('Enter a Number'))
if f>0:
    print('POSITIVE')
else :
    print('NON-POSITIVE')
"""
#2.PYTHON SCRIPT TO CHECK WHETHER A NUMBER IS DIVISIBLE BY 5 OR NOT
"""x=int(input('Enter a Number'))
if x%5==0:
    print('DIVISIBLE')
else :
    print('NON-DIVISIBLE')"""

#3.PYTHON SCRIPT TO CHECK WHETHER A NUMBER IS EVEN OR ODD
"""x=int(input('Enter a Number'))
if x%2==0:
    print('EVEN')
else :
    print('ODD')"""

#4.PYTHON SCRIPT TO CHECK GREATER BETWEEN TWO NUMBERS
"""x=int(input('Enter a Number'))
y=int(input('Enter a Number'))
if x>y:
    print(x)
else:
    print(y)"""

#5.Python Script to print two Strings in Dictionary Order    
"""a=input("Enter a String")
b=input("Enter a String")
if(a<b):
    print(a,b)
else:
    print("\n",b,a)"""


#6.PYTHON SCRIPT TO CHECK WHETHER A NUMBER IS THREE DIGIT NUMBER OR NOT
"""a=int(input('Enter a number'))
if a<1000 or a>99:
    print('Three Digits Number')"""

#7.PYTHON SCRIPT TO CHECK WHETHER A NUMBER IS POSTIVE NEGATIVE OR ZERO
"""f=int(input('Enter a Number'))
if f>0:
    print('POSITIVE')
elif f<0:
    print('NEGATIVE')
else:
        print('ZERO')"""

# 8.write a program to check whether roots of a given quadratic euation are real 
# distinct, real & equal or imaginary roots.
"""from logging import root
from math import sqrt
print("Enter Coeficients")
a=int(input());b=int(input());c=int(input())
disc=(b**2)-(4*a*c)
if disc>0:
    root1 = (-b+ sqrt(disc))/(2*a)
    root2 = (-b+ sqrt(disc))/(2*a)
    print("Root1 =",root1,"and Root2 =",root2)
    print("Roots are Real and Distinct")
elif disc==0:
    root1=root2=-b/(2*a)
    print("Root1 =",root1,"Root2 = ",root2)
    print("Roots are real and equal")
else :
    real=-b/(2*a)
    imag=sqrt(-disc)/(2*a)
    print("Both Roots are Real and Imaginary")"""

#9.PYTHON SCRIPT TO CHECK WHETHER AN YEAR IS LEAP OR NOT
"""y=int(input('Enter an year'))
if y%100==0:
    if y%400==0:
        print('Leap Year')
    else:
        print('NOT AN LEAP YEAR')
else:
    if y%4==0:
     print('Leap Year')
    else:
     print('NOT AN LEAP YEAR')"""

#10.PYTHON SCRIPT TO CHECK GREATER NUMBER AMONG THREE NUMBERS
"""a=int(input('Enter first Number'))
b=int(input('Enter second Number'))
c=int(input('Enter third Number'))

if a>b and a>c:
        print(a)
elif b>c:
        print(b)
else:
        print(c)"""


#11.PYTHON SCRIPT TO PRINT MONTH'S DAYS BY ENTERING MONTH'S VALUE
"""month=int(input('Enter a Month Value'))
if month==1 or month==1 or month== 3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print('31 Days')
elif month==4 or month==6 or month==9 or month==11 :
    print('30 Days')
elif month==2:
    print('28/29 Days')
else:
    print('Invalid Choice')"""


#12.PYTHON SCRIPT TO CHECK IF REAL OR IMAGINARY PART IS GREATER

"""d=complex(input('Enter a Complex Number'))
if d.real>d.imag:
    print('REAL')
else:
    print('IMAG')"""

