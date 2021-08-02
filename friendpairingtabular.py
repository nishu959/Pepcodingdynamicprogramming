n = int(input())
dp = [None for i in range(n+1)]

dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
  ans = dp[i-1] + (i-1)*dp[i-2]
  dp[i] = ans
 

print(dp[n])

