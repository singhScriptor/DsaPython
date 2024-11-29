# Question:selection Sort method

# Write a program to sort the array in descending order using Selection sort algorithm. After Sorting return the array.

# Note both the array and size is already given.

# Input:-

# [4,3,2,5,1]



# Output:-

# [5,4,3,2,1]

def selectionSort(arr):
    for i in range(len(arr)):
        temp=i
        for j in range(i,len(arr)):
            if(arr[j]>arr[temp]):
                temp=j
        ans=arr[i]
        arr[i]=arr[temp]
        arr[temp]=ans
    return arr
arr=[4,3,2,5,1]
print(selectionSort(arr))    
