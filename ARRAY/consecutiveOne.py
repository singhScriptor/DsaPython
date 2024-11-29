def consecuitiveOnes(arr):
    count=0
    maxi=0
    for i in range(len(arr)):
        if(arr[i]==1):
            count+=1
            maxi=max(maxi,count)
        else:
            count=0
    return maxi
arr=[1,1,0,1,1,1]
print(consecuitiveOnes(arr))


# Task details

# Problem Statement:

# Given a binary array nums, your task is to find the maximum number of consecutive 1's in the array.



# Constraints:

# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.


# Input Format:

# An integer n representing the size of the array.
# n space-separated integers representing the elements of the binary array.
# Output Format:

# Output an integer representing the maximum number of consecutive 1's in the array.
# Examples:

# Input:

# Array: 1 1 0 1 1 1

# Output : 3

# Explanation: In the given array, the maximum number of consecutive 1's is 3.