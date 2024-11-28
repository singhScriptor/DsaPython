def printPattern(n):
    i=1
    while(i<=n):
        j=0
        str='*'
        while(j<=n-i-1):
            str+="*"
            j+=1
        print(str)
        i+=1
    k=1
    while(k<=n):
        l=1
        str='*'
        while(l<k):
            str+='*'
            l+=1
        print(str)
        k+=1        
n=5
printPattern(n)            

#using for loop
def printPattern(n):
    for i in range(n):
        str='*'
        for j in range(n-i-1):
            str+='*'
        print(str)
    for k in range(n):
        str='*'
        for l in range(k+1-1):
            str+='*'
        print(str)
n=5
printPattern(n)
