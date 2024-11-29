def uniqueElement(arr,length):
    for i in range(length):
        flag='true'
        for j in range(length+1):
            if(i!=j and arr[i]==arr[j] ):
                flag="false"
                break
        if(flag=='true'):
            return arr[i]
    return -1
length=10
arr=[7,12,4,9,3,7,13,9,4,12,3]
print(uniqueElement(arr,length))
