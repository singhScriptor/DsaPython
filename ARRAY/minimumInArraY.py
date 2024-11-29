def minimumInArray(arr):
    mini=0
    for i in range(len(arr)):
        if(arr[i]<mini):
            mini=arr[i]
    return mini
arr=[5,6,2,9,-2]
print(minimumInArray(arr))