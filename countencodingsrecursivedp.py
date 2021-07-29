p = input()
dp = [None for i in range(len(p)+1)]

def k(i, n, p,dp):
  if(i>n):
    return 1
  
  if(p[i]=="0"):
    return 0
   
  if(i==n):
    
    return 1
  
  if dp[i]!=None:
    return dp[i]
  
  if(i<n and (int(p[i]) ==2 and int(p[i+1]) <=6) or int(p[i])==1):
    dp[i] = k(i+1, n, p,dp) + k(i+2, n, p,dp)
    
    
  elif(i < n and int(p[i]) >= 2):
    dp[i] = k(i+1, n, p,dp)
    
  return dp[i]

p = p.strip() 
l = k(0, len(p)-1, p,dp)
print(l)