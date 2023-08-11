# 1. tup=("Java","python","SQL","C")

# 2. tup=("C++")

"""3.
Reverse a Tuple
tup=("Java","python","SQL","C")
tup1=tup[::-1]
print(tup1)"""

"""4.
a=("java")
b=("C")
a,b=b,a
print(a,b,sep=' ')
"""

"""5.
a=(10,10,10,11)
l1=list(a)
flag=True
for i in range(0,len(l1)-1):
    if l1[i]!=l1[i+1]:
        flag=False
        break
if flag:
    print("Same")
else:
    print("Not Same")"""

"""6.
inputTuple=(100,200,300,400)
print(inputTuple)
n=1
resultTuple=tuple(inputTuple[i:i+n] for i in range(0,len(inputTuple)))
print(resultTuple)"""

"""7.
a=(1,2,3,4,5,6)
resultTuple=tuple(a[i:5:3] for i in range(3,len(a)-1))
print(resultTuple)
"""

"""8.
tuple1=(('a',21),('b',37),('c',11),('d',29))
sorted_tuple=tuple(sorted(tuple1,key=lambda x:x[1]))
print(sorted_tuple)"""

"""9.
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple1[1][1])"""

"""10.
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)"""

