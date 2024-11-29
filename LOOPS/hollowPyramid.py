def hollowPyramid(n):
    for i in range(n):
        str=''
        for j in range(n-i):
            str+=' '
        if(i==n-1):
            for k in range(2*n-1):
                str+='*'
        else:
            str+='*'
            for l in range(2*i-1):
                str+=' '
            if(i>0):
                str+='*'
        print(str)   
n=4
hollowPyramid(n)                             