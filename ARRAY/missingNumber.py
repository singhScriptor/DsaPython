def missingNumber(arr):
    arr.sort()
    for i in range(len(arr)):
        if(arr[i] != i):
            return i
    return -1    
arr=[9,6,4,2,3,5,7,0,1]
print(missingNumber(arr))


# Task details

# Problem Statement:

# Given an array nums containing n distinct numbers in the range [0, n], 
# your task is to find the missing number in the array.


# Constraints:

# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= n
# All the numbers in nums are distinct.


# Input Format:

# An integer n representing the size of the array.
# n space-separated integers representing the elements of the array.


# Output Format:

# Output an integer representing the missing number in the array.


# Examples:

# Input:

# Array: 9 6 4 2 3 5 7 0 1

# Output : 8

# Explanation: In the given array, the missing number is 8.


