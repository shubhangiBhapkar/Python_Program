#positional arguments
def addp(a,b):
    c=a+b
    print(c)
addp(2,3)

#keyword argument
def sub(a,b):
    c=a-b
    print(c)
sub(b=10,a=5)

#default argument
def mul(a,b=1):
    print(a*b)
mul(2)

#arbitary length argument
def addn(*num):
    sum=0
    for n in num:
        sum+=n
    print(sum)
addn(1,2)

#cube
def cube(n):
    return n*n*n
print(cube(2))

#lambda function

increment=lambda x : x + 1
print(increment(5))

force= lambda m,a :m*a
print(force(10,5))