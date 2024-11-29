def equalitiya(arr1,arr2):
    if(len(arr1) != len(arr2)):
        return False
    for i in range(len(arr1)):
        if(arr1[i] != arr2[i]):
            return False
    return True
arr1=3,7,2,8,6
arr2=3,7,2,9,6
print(equalitiya(arr1,arr2))

# Problem:

# In the mystical land of Equalityia, 
# where harmony was the cornerstone of existence, 
# a magical quest was underway. 
# The citizens of Equalityia held two sacred arrays, 
# each representing the essence of balance and equality in their realm. 
# However, whispers of uncertainty echoed through the air as doubts arose about the equality of these arrays.

# To ensure the continued prosperity of Equalityia, 
# it was essential to verify whether the two arrays were truly equal. Each element in the arrays had a unique magical property, and for Equalityia to maintain its serene balance, every element in both arrays needed to align perfectly.

# Input:

# In the heart of Equalityia, 
# where magic is intertwined with reality, 
# your task is to create a function that can scrutinize the magical arrays. 
# The function will receive the following:

# 1. An array `arr1` of size `n` (1 ≤ n ≤ 10^5), 
# represents the elements of the first array in Equalityia.

# 2. An array `arr2` of size `m` (1 ≤ m ≤ 10^5), 
# represents the elements of the second array in Equalityia.


# Output:

# Your magical function should determine whether the arrays are equal or not. 
# If every element in both arrays aligns perfectly,
# the function should return a signal confirming their equality. 
# If there are any disparities, 
# the function should gracefully communicate this to the citizens of Equalityia.

# Example:

# Input:

# 3 7 2 8 6

# 3 7 2 8 6

# Output

# True