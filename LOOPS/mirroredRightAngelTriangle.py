def rightAngelTriangle(n):
    for i in range(n):
        str=''
        for j in range(i):
            str+=' '
        for k in range(n-i):
            str+='*'
        print(str)
n=4
rightAngelTriangle(n)

# while loop 
def triangle(m):
    i=0
    while(i<m):
        j=0
        str=''
        while(j<i):
            str+=' '
            j+=1
        k=0
        while(k<m-i):
            str+='*'
            k+=1
        print(str )
        i+=1
m=6
triangle(m)           

