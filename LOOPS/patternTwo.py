def printPattern(n):
    for i in range(1,n+1):
        st=''
        for j in range(1,i*2):
            st+=str(i)
        print(st)
n=5
printPattern(n)


# for loop 
def printPattern(m):
    i=1
    while(i<=m):
        st=''
        j=1
        while(j<i*2):
            st+=str(i)
            j+=1
        print(st)
        i+=1
m=5
printPattern(m)            
