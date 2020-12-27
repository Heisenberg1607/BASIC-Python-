from functools import reduce
lst=[]
n = int(input("enter the length of your list:"))

for i in range(0,n):
    x= int(input("enter the numbers:"))
    lst.append(x)
print("this is the original list:",lst)

even = list(filter(lambda n: n%2==0,lst))
print("this is the even number list:",even)

doubles=list(map(lambda n: n*2,lst))
print("this is the doubled list",doubles)

sum= reduce(lambda n,m: n+m, lst)
print("this is the sum of the list", sum)

print("OK BYE!")

