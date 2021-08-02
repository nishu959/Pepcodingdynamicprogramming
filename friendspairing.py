n = int(input())
dp = [None for i in range(n+1)]


def pair(n,dp):
  
  if(n==2 or n==1):
    return n
  
  if(dp[n]!=None):
    return dp[n]
  
  
  ans1 = pair(n-1, dp)
  ans2 = (n-1)*pair(n-2, dp)
  ans = ans1 +ans2
  
  dp[n] = ans
  return ans
 
print(pair(n,dp))

