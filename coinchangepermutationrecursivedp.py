m = int(input())

coins = []

for i in range(m):
  coins.append(int(input()))
  
target = int(input())

dp = [None]*(target+1)

def percoin(target):
  if(target ==0):
    
    return 1
    
  if(target<0):
    return 0
  
  if(dp[target]!=None):
    return dp[target]
   
  ans = 0 
  for i in coins:
    ans += percoin(target-i)
  
  dp[target] = ans 
  return ans 
    

print(percoin(target)) 
    
    