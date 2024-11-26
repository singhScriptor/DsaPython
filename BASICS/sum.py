def sum(a,b):
    return a+b
a,b=7,-3
print(sum(a,b))

# recursion
def recursiveSum(m,d):
    if(d==0):
        return m
    elif d > 0:
        return recursiveSum(m+1,d-1)
    return recursiveSum(m-1,d+1)
m,d=7,-4
print(recursiveSum(m,d))