# def printPattern(n):
#     i=0
#     while(i<n):
#         j=0
#         str='*'
#         while(j<i):
#             str+='*'
#             j+=1
#         k=0
#         while(k<n-i-1):
#             str+=' '
#             k+=1
#         l=0
#         while(l<=i):
#             str+='*'
#             l+=1
#         print(str)
#         i+=1        

# n=5
# printPattern(n)

# for loop

def printPattern(n):
    for i in range(n):
        str='*'
        for j in range(i):
            str+="*"
        for k in range(n-i-1):
            str+=' '
        for l in range(i+1):
            str+='*'
        print(str)        
n=5
printPattern(n)            

