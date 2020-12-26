
x= int(input("enter a number"))  
def facto(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
  
result=facto(x)        
print(result)

