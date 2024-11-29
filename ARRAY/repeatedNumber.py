# Problem:

# Amidst the digital labyrinth of Codeville, 
# a town steeped in algorithmic wonders,
# the talented programmer Alex found themselves facing a new enigma.
# Deep within the data dungeons, an array encrypted with cryptic values held the key to unraveling an ancient code. 
# Legend whispered that a specialized function could be the beacon guiding Alex to the heart of this puzzle, 
# where a crucial element awaited—a key that would unlock the secrets of the ages.



# The mission was clear for Alex: forge a function with the ability to navigate through the cryptic array, 
# pinpointing the exact location of the elusive first duplicate element. 
# The town's fate hinged on discovering this element, 
# as it held the power to decode the secrets encrypted within the ancient code.

# Input:

# An integer n (1 ≤ n ≤ 10^5), represents the size of the mystical array.
# A line of n space-separated integers, each holding a piece of information within the array.


# Output:

# Alex's function should return the value of the first duplicate element within the mystical array. 
# If no duplicates are found, the function should gracefully signal -1, suggesting that the secrets of the ancient language may be hidden deeper within the array.

# Example:

# Input:

# 10

# 7 23 15 42 7 56 89 15 91 42

# Output:7

def repeatedNumber(arr,length):
    arr.sort()
    for i in range(length):
        if(arr[i]==arr[i+1]):
            return arr[i]
    return -1
length=10
arr=[7,23,15,42,7,56,89,15,91,42]
print(repeatedNumber(arr,length))    
