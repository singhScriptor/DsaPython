def sum(a,b):
    return a+b
a,b=10,30
print(sum(a,b))

# recursion
def recursiveSum(m,d):
    if(d==0):
        return m
    return recursiveSum(m+1,d-1)
m,d=34,67
print(recursiveSum(m,d))