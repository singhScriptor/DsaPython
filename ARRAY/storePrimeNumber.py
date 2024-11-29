def primeNumbers(n):
    arr=[]
    x=2
    count=0
    while(len(arr)<n):
        flag='true'
        for i in range(2,x):
            if((x%i)==0):
                flag="false"
                break
        if(flag=='true'):
            arr.append(x)
            count+=1
        if(count==n):
            break
        x+=1
    return arr
n=5
print(primeNumbers(n))