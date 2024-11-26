def printDigit(n):
    while(n):
        temp=n%10
        n=n//10
        print(temp)
n=153
printDigit(n)


# recursion

def Digit(m):
    if(m==0):return
    print(m%10)
    Digit(m//10)
m=351
Digit(m)    