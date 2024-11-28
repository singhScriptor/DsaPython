def printPattern(n):
    i=0
    while(i<n):
        j=i
        str='*'
        while(j<n-1):
            str+="*"
            j=j+1
        print(str)
        i+=1
n=5
printPattern(n)

# forloop
def printPattern(m):
    for i in range(m):
        str='*'
        for j in range(m-i-1):
            str+="*"
        print(str)
m=5
printPattern(m)

