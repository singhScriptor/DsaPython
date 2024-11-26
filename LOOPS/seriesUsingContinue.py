def print_Series(n):
    i=1 
    while(i<=n):
        if(i%5==0):
            i+=1
            continue
        print(i)
        i+=1
n=7
print_Series(n)      

# recursion

def series(n):
    def loop(i):
        if(i>n): 
            return
        if (i%5 != 0):
            print(i)
        i+=1
        loop(i)
    loop(1)        
def main():
    m=7
    series(m)
main()


