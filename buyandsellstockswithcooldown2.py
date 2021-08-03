n = int(input())
l = []

for i in range(n):
  l.append(int(input()))
 

dp =[[None for i in range(3)] for j in range(n+1)]


dp[0][0] = -1 * l[0]
dp[0][1] = 0
dp[0][2] = 0


for i in range(1,n+1):
  
  dp[i][0] = max(dp[i-1][0], dp[i-1][2] - l[i-1])
  
    
  dp[i][1] = max(dp[i-1][1], l[i-1] + dp[i-1][0])
    
   
  dp[i][2] = max(dp[i-1][1],dp[i-1][2])
  
  

print(dp[n][1])

