def typesOfBurger(X,Y,N,R):
    for normal in range(N+1):
        premium=N-normal
        if(normal*X + premium*Y==R):
            return (normal,premium)
    return -1    
X,Y,N,R=2,10,4,12
print(typesOfBurger(X,Y,N,R))        