def multiple():
    for i in range(2,4+1):
        table=''
        for j in range(1,10):
            table+=str(i*j)+' '
        print(table)
multiple()
