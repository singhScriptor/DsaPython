#while loop
def evenNumber(n):
    i=1
    while(i<=n):
        if(i%2==0):
            print(i)
        i+=1
n=10
evenNumber(n)            


# recursion

def printEven(n):
    def odd(i):
        if(i>n):
            return 
        print(i)
        odd(i+2)
    odd(2)    
def main():
    m=14
    printEven(m)
main()    