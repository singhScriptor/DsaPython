def armStrong(n):
    temp=n
    sum=0
    while temp:
        i=temp%10
        sum=sum+i**3
        temp=temp//10
    return n==sum
n=153
print(armStrong(n))
    