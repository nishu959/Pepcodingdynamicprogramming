s = int(input())

def tabulation(s):
  dp = [None]*(s+1)
 
  dp[0] = 0
  dp[1] = 1
 
  for i in range(2,s+1):
    dp[i] = dp[i-1] + dp[i-2]
  
  return dp[s]
  
 
 
print(tabulation(s)) 
  