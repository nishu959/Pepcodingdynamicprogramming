m = int(input())

coins = []

for i in range(m):
  coins.append(int(input()))
  
target = int(input())

dp = [[None for i in range(target+1)] for j in range(m+1)]

def comcoin(target, coin):
  if(target ==0):
    
    return 1
    
  if(target<0):
    return 0
  
  if(dp[coin][target]!=None):
    return dp[coin][target]
  
  ans = 0 
  for i in range(coin, len(coins)):
    ans += comcoin(target-coins[i], i)
  
  dp[coin][target]= ans 
  return ans 
    

print(comcoin(target, 0)) 


    
    