# 1.
"""month=int(input("Enter a Month Number"))
match month:
    case 1:
        print("31 Days")
    case 3:
        print("31 Days")
    case 5:
        print("31 Days")
    case 7:
        print("31 Days")
    case 8:
        print("31 Days")
    case 10:
        print("31 Days")
    case 12:
        print("31 Days")
    case 4:
        print("30 Days")
    case 6:
        print("30 Days")
    case 9:
        print("30 Days")
    case 11:
        print("30 Days")
    case 2:
        print("28/29 Days")
    case _:
        print("Invalid Month Number")"""

# 2.
"""print("1.Press 1 To Add Two Numbers\n2.Press 2 To Subtract Two Numbers\n3.Press 3 To Multiply Two Number\n4.Press 4 To Divide Two Numbers")
x=int(input("Enter YOur Choice"))
match x:
    case 1:
        a,b=eval(input("Enter a Number")),eval(input("Enter Second Number"))
        print("Sum is ",a+b)
    case 2:
        a,b=eval(input("Enter a Number")),eval(input("Enter Second Number"))
        print("Difference is ",a-b)
    case 3:
        a,b=eval(input("Enter a Number")),eval(input("Enter Second Number"))
        print("Product is ",a*b)
    case 4:
        a,b=eval(input("Enter a Number")),eval(input("Enter Second Number"))
        print("Division is ",a//b)"""

# 3.
"""print("Enter Three Sides of a Triangle")
print("Press 1. To Check if it's an Isoceles Triangle or not")
print("Press 2. To Check if it's a right Angled triangle or not")
print("Press 3. To Check if it's an equilateral Triangle ot not")
print("Press 4. To EXIT")
x=eval(input())
match x:
    case 1:
        a,b,c=eval(input("Enter First Side")),eval(input("Enter Second Side")),eval(input("Enter Third Side"))
        if a==b and b!=c or b==c and c!=a or c==a and a!=b:
            print("Isoceles Triangle")
        else :
            print("Not an Isoceles Triangle")
    case 2:
        a,b,c=eval(input("Enter First Side")),eval(input("Enter Second Side")),eval(input("Enter Third Side"))
        if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
            print("Right Angeled Traingle")
        else :
            print("Not a Right Angeled Triangle")
    case 3:
        a,b,c=eval(input("Enter First Side")),eval(input("Enter Second Side")),eval(input("Enter Third Side"))
        if a==b and b==c:
            print("Equitaleral Traingle")
        else :
            print("Not an Equilateral Triangle")
    case 4:
        exit"""

# 4.
"""age=int(input("Enter Your age"))
match (age>=60):
    case 1:
        print("Senior Citizen")
    case 0:
        match (40<age<60):
            case 1:
                print("Experienced")
            case 0:
                match (20<age<40):
                    case 1:
                        print("Young")
                    case 0:
                        match (age<20):
                            case 1:
                                print("Teen")
                            case 0:
                                match (age<10):
                                    case 1:
                                        print("Kid")"""

#5.
"""user_input=int(input("Enter a Number"))
match user_input%2:
    case 0:
        print("Saurabh Shukla")
    case 1:
        match (user_input<0):
            case 1:
                print("Prateek Jain")
            case 0:
                print("Aditya Choudhary")"""

#6
"""string=input()
match (' ' in string):
    case 1:
        print("Multi Word String")
    case 0:
        print("Single Word String")"""

#7
"""n=int(input())
match n>0:
    case 1:
        print("Positive")
    case 0:
        match (n==0):
            case 1:
                print("Zero")
            case 0:
                print("negative")"""

#8
"""str1=input()
str2=input()
match str2>str1:
    case 1:
        print("First String comes before Second String")
    case 0:
        match (str2==str1):
            case 1:
                print("Identical Strings")
            case 0:
                print("Second String Comes Before First String")"""

#9
"""year=int(input())
match year%4==0:
    case 1:
        match year % 100 == 0:
            case 1:
                match year % 400==0:
                    case 1:
                        print("Century Leap Year")
            case 0:
                print("Non-Century leap year")
    case 0:
        match year%100!=0:
            case 1:
                print("Non Century Non Leap Year")
            case 0:
                print("Centur Non Leap Year")"""

#10
"""color=input("favourite Color")
match "red" in color:
    case 1:
        print("Saturday")
    case 0:
        match "black" in color:
            case 1:
                print("Friday")
            case 0:
                match "yellow" in color:
                    case 1:
                        print("Monday")
                    case 0:
                        match  "blue" in color:
                            case 1:
                                print("Tuesday")
                            case 0:
                                match "orange" in color:
                                    case 1:
                                        print("Wednesday")
                                    case 0: 
                                        match "white" in color:
                                            case 1:
                                                print("Thursday")
                                            case 0:
                                                print("Sunday")"""    

