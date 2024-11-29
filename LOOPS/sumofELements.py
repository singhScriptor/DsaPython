# Problem:



# In the domain of numerical challenges, you are tasked with a mission to compute the sum of elements in an integer array.



# Input:



# The input consists of two lines:



# 1. The first line contains an integer `n` (1 ≤ n ≤ 10^5), representing the size of the array.



# 2. The second line contains `n` space-separated integers, each denoting an element of the array.



# Output:



# Your objective is to output a single integer, representing the sum of all elements in the given array.



# Example:



# Input:



# 6

# 4 7 2 9 1 5



# Output:



# 28

def elementSum(arr,n):
    sum=0
    for i in range(n):
        sum+=arr[i]
    return sum
n=6
arr=[]
for i in range(n):
    arr.append(int(input()))
print(elementSum(arr,n))