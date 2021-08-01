n =int(input())

dp = [[None for i in range(n+1)]for j in range(n+1)]

def fun(ip,op, n, dp):
  
  if(op == n):
    return 1
  if(op>n):
    return 0
    
  
  
  if(dp[ip][op]!=None):
    return dp[ip][op]
  
  
  op1 = op + 1
  op2 = op + 2
  p = fun(ip +1,op1,n, dp)
  q = fun(ip +1,op2,n, dp) 
  
  dp[ip][op] = p+q
  
  return p+q
  
   
p = fun(0,0,n, dp)

print(int(p))

