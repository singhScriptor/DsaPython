# Question (Insertion Sort Method)

# Write a program to sort the array in ascending order using Insertion sort algorithm. After Sorting return the array.

# Note both the array and size is already given.

# Input:-

# [4,3,2,5,1]



# Output:-

# [1,2,3,4,5]

def insertionSort(arr):
    for i in range(len(arr)):
        temp=arr[i]
        j=i-1
        while(j>=0 and temp<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    return arr
arr=[5,3,1,4,2]
print(insertionSort(arr))