def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial
n=5
print(factorial(n))  

# while loop
def factorial(n):
    i=1
    fact=1
    while(i<=n):
        fact*=i
        i=i+1
    return fact
n=8
print(factorial(n))    

        