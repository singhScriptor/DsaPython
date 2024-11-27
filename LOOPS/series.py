def SERIES(n):
    i=1
    while(i<=n):
        if(i*i*i<=n):
            print(i*i*i)
        i+=1
n=125
SERIES(n)

# for loop
def serieS(m):
    for i in range(1,m+1):
        if(i*i*i<=m):
            print(i*i*i)
m=64 
serieS(m)           