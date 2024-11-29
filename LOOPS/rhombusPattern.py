def rhombus(n):
    for i in range(n):
        str=''
        for j in range(n-i):
            str+=' '
        for k in range(n):
            str+='*'
        print(str)
n=4
rhombus(n)