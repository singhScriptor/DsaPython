def maxiWealth(accounts):
    maxi=0
    for i in range(len(accounts)):
        total=sum(accounts[i])
        maxi=max(maxi,total)
    return maxi
accounts=[[1,2,3],[3,2,1]]
print(maxiWealth(accounts))        
                   