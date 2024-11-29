def maxiSum(arr):
    mSum=0
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum+=arr[j]
            if(sum>mSum):
                mSum=sum
    return mSum
arr=[5,2,-4,-5,3,-1,2,3,1]
print(maxiSum(arr))