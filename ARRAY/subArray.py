def subArray(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            st=''
            for k in range(i,j+1):
                st+=str(arr[k])
            print(st)
arr=[1,2,3,4,5]
subArray(arr)                