def sumOfMultiples(N,X):
    sum=0
    for i in range(N):
        if(i%X==0):
            sum+=i
    return sum
N,X=10,3
print(sumOfMultiples(N,X))
        
