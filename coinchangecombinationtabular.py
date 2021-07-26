m = int(input())

coins = []

for i in range(m):
  coins.append(int(input()))
  
target = int(input())

dp = [0]*(target+1)

dp[0] = 1

for i in coins:
  for j in range(i, target+1):
    
    dp[j]+=dp[j-i]
    
    
print(dp[target])
  