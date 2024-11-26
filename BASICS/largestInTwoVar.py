# adding message in return using this method:
#   return f"Largest Number is : {b}"

def findLargest(a,b):
    if(a>b):
        return f"Largest Number is : {a}"
    return f"Largest Number is : {b}"
def main():
    a,b=43,89
    print(findLargest(a,b))
main()    

# 2nd method
## terenary operator
def Largest(a,b):
    return f"Largest Number is : {a}" if (a>b) else f"Largest Number is : {b}"
def main():
    c,d=45,29
    print(Largest(c,d))
main()    