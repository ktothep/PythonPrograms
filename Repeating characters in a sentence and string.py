#Counter is basically used to get the number of elements which are present in the string
#most common gives the topmost elements which are repeating in the string
#we can use it to find the repeating elements in the string


from collections import Counter
s=input("Enter a string")
list=[]
for k in s:
    list.append(k)
print(list)

x=Counter(list)
print(x)
a=0
for i,j in x.items():
    if j>1:
        print(i)


s1=input("Enter a string")
list1=[]
for k1 in s1.split(" "):
    list1.append(k1)
print(list1)
x1=Counter(list1)
print(x1)
a1=0
for i1,j1 in x1.items():
    if j1>1:
        print(i1)
