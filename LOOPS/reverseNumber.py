def reverseNumber(n):
    rev=0
    while(n):
        temp=n%10
        rev=rev*10+temp
        n=n//10
    return rev    
def main():
    n=321
    print(reverseNumber(n))
main()