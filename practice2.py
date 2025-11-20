#1
num=[1,2,3,4,5,6,7,8,9]
def double(x):
    return x*2
res=map(double,num)
print(list(res))
#2
num=[1,2,3,4,5,6,7,8,9]
res=map(lambda x: x*3,num)
print(list(res))

a=[1,2,3,4]
b=[5,6,7,8]
res=map(lambda x,y: x+y ,a ,b)
print(list(res))

#filter
#even
num=[3,4,5,6]
def is_even(x):
    return x%2==0
res=filter(is_even,num)
print(list(res))
#odd
num=[3,4,5,6]
def is_odd(x):
    return x%2!=0
res=filter(is_odd,num)
print(list(res))

#using lambda function
num=[3,4,5,6]
res=filter(lambda x: x%2==0 ,num)
print(list(res))

#Reduce
from functools import reduce
num=[6,8,6,5,4,2]
def add(x,y):
    return x+y
res=reduce(add,num)
print(res)

from functools import reduce
num=[6,8,6,5,4,2]
res=reduce(lambda x,y: x if x>y else y,num)
print(res)

#practical exmple
from functools import reduce
scores=[85,32,6,75,88,15,11]

updated=list(map(lambda x:x+10 , scores))
passed=list(filter(lambda x:x>=35,updated))
total=reduce(lambda x,y:x+y,passed)

print("Updated scores:",updated)
print("Passed Students:",passed)
print("Total score:",total)