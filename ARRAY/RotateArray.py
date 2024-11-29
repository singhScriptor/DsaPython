def rotateArr(nums,k):
    k=k%len(nums)
    rotated=nums[-k:]+nums[:-k]
    for i in range(len(nums)):
        nums[i]=rotated[i]
    return nums
nums=[1,2,3,4,5,6,7]
k=3
print(rotateArr(nums,k))    
