## for loop

def fibonacci(n):
    a,b=0,1
    for i in range(2,n):
        temp=a+b
        a=b
        b=temp
    return b
n=6
print(fibonacci(n))

# Recusrsion method
def fibonacci(m):
    if(m<=1):return m
    return fibonacci(m-1)+fibonacci(m-2)
m=9
print(fibonacci(m))


