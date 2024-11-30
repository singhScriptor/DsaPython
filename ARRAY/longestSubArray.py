def longestSubArray(arr):
    left=0
    maxi=0
    jrr={}
    for i in range(len(arr)):
        if(arr[i] in jrr and jrr[arr[i]]>=left):
            left=jrr[arr[i]]+1
        jrr[arr[i]]=i 
        maxi=max(maxi,i-left+1) 
    return maxi
arr=[1,2,3,1,2,3,4,5]
print(longestSubArray(arr))


# Task details

# Problem Statement:

# Given an array of integers nums, your task is to find the length of the longest subarray such that all elements in the subarray are distinct digits (0-9).


# Constraints:

# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 9


# Input Format:

# An integer n representing the size of the array.
# n space-separated integers representing the elements of the array.


# Output Format:

# Output an integer representing the length of the longest subarray without repeat digits.


# Examples:

# Input:

# Array: 1 2 3 1 2 3 4 5

# Output : 5

# Explanation: The longest subarray without repeat digits is [1 2 3 4 5].

