def evenNumber(n):
    i=1
    while(i<=n):
        if(i%4==0):
            i+=1
            continue
        if(i%2==0):
            print(i)
        i+=1    

n=10
evenNumber(n)

# for loop
def EvenNumber(m):
    for i in range(m+1):
        if(i%4==0):
            continue
        if(i%2==0):
            print(i)
m=10
EvenNumber(m)            