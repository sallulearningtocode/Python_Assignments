"""1.
list=[]
for i in range(1,int(input())+1):
    list.append(i)
print(list)"""

"""2.
list=[]
for i in range(1,int(input())+1):
    list.append(i*2-1)
print(list)"""

"""3.
list=[]
for i in range(1,int(input())+1):
    list.append(i*2)
print(list)"""

"""4.
g=max([10,20,30,40,550,60,11,12,111])
print(g)"""

"""5.
g=min([10,20,30,40,550,60,11,12,111])
print(g)"""

"""6.
print(sum([10,20,30,40,50]))"""

"""7.
Write a python script to remove all non int values from a list.
list1=["Salman Khan",1,"Neha Kumari",2,"Aman Kumar",3]
for x in list1:
    if type(x)!=int:
        list1.remove(x)
print(list1)"""

"""8.
l1=[10,20,30,10,20,50,60,70,80,80,80,80]
l1.sort()
for i in range(0,len(l1)-1):
    if l1[i]!=l1[i+1]:
        print(l1[i],l1.count(l1[i]),sep=' ')
print(l1[-1],l1.count(l1[-1]),sep=' ')"""

"""9.
n=int(input())
l1=[10,10,20,30,40,10,50,40,60,70,80,10,20,10]
for i in range(0,len(l1)):
    if n==l1[i]:
        print(i)"""

"""10.
l1=[10,20,50,60,11,48,98]
l1.sort()
print(l1)"""