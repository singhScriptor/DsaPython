def perfectSq(n):
    i=1
    while(i<=n):
        if(i*i<=n):
            print(i*i)
        i+=1
n=49
perfectSq(n)

# recursion

def perfectSquare(m):
    def square(j):
        if(j*j>m):return 
        print(j*j)
        square(j+1)
    square(1) 
m=49
perfectSquare(m)
