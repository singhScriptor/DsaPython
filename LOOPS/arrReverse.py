# Problem



# Raju, a diligent student, 
# is faced with a peculiar task from his teacher. 
# The challenge is to reverse the order of elements in an array. 
# Knowing your knack for problem-solving, Raju seeks your assistance to conquer this array manipulation quest.



# Can you help Raju by implementing a function that returns a new array with the reversed order of elements?



# Input:



# Raju provides you with the following details:



# 1. An integer `n` (1 ≤ n ≤ 10^5), representing the size of the array.

# 2. A line of `n` space-separated integers, each symbolizing an element of the array.



# Output:



# Your mission is to implement a function `reverse_array` that takes the size of the array and the array elements as input and returns a new array with the reversed elements.



# Example:



# Input:

# 6

# 17 32 9 5 21 14



# Output:

# 14 21 5 9 32 17


def reverseArray(arr):
    left = 0 
    right=len(arr)-1
    while left < right:
        temp=arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left+=1
        right-=1
    return arr
arr=[17,32,9,5,21,14]
print(reverseArray(arr))