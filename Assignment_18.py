"""1.
myInfo={'Name':"Salman",'Age':21,'Gender':"Male"}
print(myInfo)"""

"""2.
myInfo={'Name':"Salman",'Age':21,'Gender':"Male"}
print(myInfo['Name'])"""

"""3.
myInfo={'Name':"Salman",'Age':21,'Gender':"Male"}
print([(myInfo[i]) for i in myInfo])
"""

"""4.
myInfo={'Name':"Salman",'Age':21,'Gender':"Male"}
myInfo['Gender']=22
print(myInfo['Gender'])"""

"""5.
myInfo={'Name':"Salman",'Age':21,'Gender':"Male"}
for i in myInfo:
    print(i,end=' ')"""

"""6.
Make Dictionary of Dictionaries
dict1={"Dict1":{'Value':1},"Dict2":{'Value':2},"Dict3":{'Value':3}}
print(dict1)"""

"""7.
Make Dictionary of Dictionaries
dict1={"Person_Name":{"name":'Salman'},"Person_Age":{"Age":22},"Person_Grades":{"Grade":'A+'}}
dict2={"School_Name":{"name":'RMPS'},"School_Medium":{'Medium':'ENGLISH'},"Is_Recognized":{'recognition':'Yes'}}
dict3={"College_Name":{"Name":'IGNOU'},"College_Medium":{'Medium':'English'},"is_Recognized":{'Recognition':'Yes'}}
dict4={"Dict1":dict1,"Dict2":dict2,"Dict3":dict3}
print(dict4)"""

"""8.
list1=['Name','Age','E-Mail']
list2=['Salman Khan',21,'khansalman@gmail.com']
my_dict = {list1[i]:list2[i] for i in range(len(list1))}
print(my_dict)"""

"""9.
dict1={'one':1,"two":2,"three":3}
dict2={'four':4,"five":5,"six":6}
dict1.update(dict2)
print(dict1)"""

"""10.
dict1={
    'C':92,
    'Java':66,
    'Python':85
}
lowest_values=list(set(dict1.values()))
result=[key for key, value in dict1.items() if value == lowest_values[0]]
print(result)"""

