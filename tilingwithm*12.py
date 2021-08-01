n =int(input())
m = int(input())

dp = [[None for i in range(n+1)]for j in range(n+1)]

def fun(ip, op, m, n, dp):
  
  if(op ==n ):
    return 1
    
  if(op>n):
    return 0
  
  
  if(dp[ip][op]!=None):
    return dp[ip][op]
  
  
    
  p = fun(ip+1,op+1,m, n, dp)
  q = fun(ip+1,op+m,m ,n, dp)

  dp[ip][op] = p+q
  return p+q
  
  
  
   
p = fun(0,0,m,n, dp)

print(int(p))

