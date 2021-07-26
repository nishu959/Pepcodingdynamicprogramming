m = int(input())

coins = []

for i in range(m):
  coins.append(int(input()))
  
target = int(input())
 
dp = [0]*(target+1)
dp[0] = 1

for tar in range(1,target+1):
  for coin in coins:
    
    if(coin<=tar):
      rem = tar - coin
      dp[tar] += dp[rem]
      
     


print(dp[target])
