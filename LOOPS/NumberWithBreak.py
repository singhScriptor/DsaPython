def numbers(n,m):
    i=0
    while i<=n:
        if(i==m):
            break
        i+=1
        print(i)
def main():
    n,m=10,4
    numbers(n,m)
main()

# for loop 
def numbers(n,m):
    for i in range(1,n):
        if(i==m):
            break
        print(i)
def main():
    j,k=10,4 
    numbers(j,k)
main()           
