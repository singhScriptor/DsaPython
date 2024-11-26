#by terenary Operator
def findLargest(a,b,c):
    return f"largest is a: {a}" if (a>b) and (a>c) else f"largest is b: {b}" if(b>a) and (b>c) else f"largest is c: {c}"
a,b,c=34,56,12
print(findLargest(a,b,c))

##else if

def largest(d,e,f):
    if(d>e) and (d>f):
        return f"Largest is d: {d}"
    elif(e>d) and (e<f):
        return f"Largest is e: {e}"
    else:
        return f"Largest is f: {f}"
def main():
    d,e,f=15,9,18
    print(largest(d,e,f))
main()    
