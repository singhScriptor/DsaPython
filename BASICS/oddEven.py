def findOddEven(n):
    if(n % 2 == 0):
        return 'Even'
    else:
        return 'Odd'
n=14
print(findOddEven(n))    

# terenary operator
def oddEven(v):
    return 'Even' if v%2 == 0 else "Odd"
v=12
print(oddEven(v))

