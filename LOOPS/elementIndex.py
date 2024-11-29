# Problem:

# In the quaint village of Algorithmica, there lies a treasure chest guarded by an ancient array. Legend has it that the key to unlocking this chest is a mystical function capable of finding the exact location of a specific element within the array.

# Embark on a journey through the mystical array and implement a function to search for a particular element. Your quest is to return the index of the sought-after element, unlocking the secrets hidden within the treasure chest.



# Input:

# You will be provided with the following clues:

# 1. An integer `n` (1 ≤ n ≤ 10^5), representing the size of the array.

# 2. A line of `n` space-separated integers, each holding a unique piece of information within the array.

# 3. A magical key, an integer `target`, represents the element you seek.

# Output:

# Your mission is to implement a function that will unveil the index of the sought-after element, providing access to the hidden treasures.

# Example:
# In your quest, you may encounter the following scenario:

# Input:
# 8

# 3 17 9 25 12 5 14 21

# 12

# Output:

# 4

def elementIndex(arr,length,target):    
    for i in range(length):
        if(arr[i]==target):
            return i
    return -1
length=8
arr=[3,17,9,25,12,5,14,21]
target=12
print(elementIndex(arr,length,target))    

