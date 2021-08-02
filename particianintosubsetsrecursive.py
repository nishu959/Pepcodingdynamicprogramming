m = int(input())
n = int(input())

dp = [[None for i in range(n+1)]for j in range(m+1)]

def fun(m, n,dp):
  
  if(m==0 or n==0):
    
    return 0
   
  if(n==1):
    return 1
    
  if(n==m):
    return 1
    
  if(n>m):
    return 0
  
  if(dp[m][n]!=None):
    return dp[m][n]
  
 
  
  ans1 = fun(m-1, n, dp) * n
  ans2 = fun(m-1, n-1,dp)
  ans = ans1 + ans2
  
  
  dp[m][n] = ans
  return ans


print(fun(m, n,dp))

