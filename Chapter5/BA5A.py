# Find the Minimum Number of Coins Needed to Make Change

def DPChangeMoney(money,coins):
    
    MinNumCoins=[0]

    for m in range(1, money+1):
        MinNumCoins.append(float("inf"))
        for i in range(1,len(coins)):
            if(m>=coins[i]):
                if MinNumCoins[m-coins[i]]+1 < MinNumCoins[m]:
                    MinNumCoins[m]=MinNumCoins[m-coins[i]]+1
                    
    return MinNumCoins[money]


unos='''40
1,5,10,20,25,50'''
unos=unos.splitlines()
money=int(unos[0])
coins=list(map(int,unos[1].split(",")))

print(DPChangeMoney(money,coins))
