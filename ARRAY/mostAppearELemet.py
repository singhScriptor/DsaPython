def mostAppear(nums):
    nums.sort()
    arr=[]
    for i in range(1,len(nums)):
        if(nums[i]==nums[i-1]):
            arr.append(nums[i])
    return arr
nums=[4,3,2,7,8,2,3,1]
print(mostAppear(nums))

# Task details

# Problem Statement:

# Given an array of integers nums containing n integers where each integer is in the range [1, n], your task is to find all the integers that appear more than once in the array.





# Constraints:

# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= n


# Input Format:

# An integer n representing the size of the array.
# n space-separated integers representing the elements of the array.


# Output Format:

# Output an array of integers representing the integers that appear more than once in the array. The elements in the output array should be in sorted in non-decreasing order.


# Examples:

# Input:

# Array: 4 3 2 7 8 2 3 1

# Output :  [2, 3]

# Explanation: In the given array, the integers 2 and 3 appear more than once.



# Example 2:

# Array: 1 1 2 2 3 3

# Output : [1, 2, 3]

# Explanation: In the given array, all integers appear more than once
