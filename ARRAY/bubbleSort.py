# Question

# Write a program to sort the array in descending order using Bubble sort algorithm. After Sorting return the array.

# Note both the array and size is already given.

# Input:-

# [4,3,2,5,1]



# Output:-

# [5,4,3,2,1]

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if(arr[j]<arr[j+1]):
                temp=arr[i] 
                arr[i]=arr[j]
                arr[j]=temp
    return arr
arr=[4,3,2,5,1]
print(bubbleSort(arr))
