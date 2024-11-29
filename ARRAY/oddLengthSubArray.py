def oddLenSubArray(arr):
    sum=0
    for i in range(len(arr)):
        total=0
        for j in range(i,len(arr)):
            total+=arr[j]
            if((j-i)%2==0):
                sum+=total
    return sum 
arr=[1,4,2,5,3]
print(oddLenSubArray(arr))