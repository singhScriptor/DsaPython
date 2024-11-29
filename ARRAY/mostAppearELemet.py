def mostAppear(nums):
    nums.sort()
    arr=[]
    for i in range(1,len(nums)):
        if(nums[i]==nums[i-1]):
            arr.append(nums[i])
    return arr
nums=[4,3,2,7,8,2,3,1]
print(mostAppear(nums))        
