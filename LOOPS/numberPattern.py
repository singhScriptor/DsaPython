def numPattern(n):
    for i in range(n):
        num=''
        for j in range(i+1):
            num+=str(j+1)
        print(num)
n=5
numPattern(n)

# while loop
def numPattern(n):
    i=1
    while(i<=n):
        into=''
        j=0
        while(j<i):
            into+=str(j+1)
            j=j+1
        print(into)
        i+=1
n=4
numPattern(n)
