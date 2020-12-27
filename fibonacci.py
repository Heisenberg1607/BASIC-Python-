
x=int(input("enter your fibo length"))
def hello(n):
    a=0
    b=1
    print(a)
    print(b)

    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
hello(x)
