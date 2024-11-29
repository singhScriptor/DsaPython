def MaxiDigitInArr(arr):
    maxi=0
    for i in range(len(arr)):
        if(arr[i]>maxi):
            maxi=arr[i]
    return maxi        

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(MaxiDigitInArr(arr))                       