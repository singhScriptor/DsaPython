def swapNumber(a,b):
    if (a and b):
        temp=a
        a=b
        b=temp
        print(a)
        print(b)
def main():
    a=25
    b=45
    swapNumber(a,b)
main()    

# 2nd method
def swapNumber(a,b):
    if(a and b):
        a,b = b,a
    return a,b      
def main():
    c=34
    d=49
    print(swapNumber(c,d))    
main()   