s = int(input())

def tabulation(s):
  dp = [None]*(s+1)
  dp[0] = 1
  
  for i in range(1,s+1):
    if(i==1):
      dp[i] = dp[i-1]
    elif(i==2):
      dp[i] = dp[i-1] + dp[i-2]
      
    else:
      dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
      
  return dp[s]
   
   
print(tabulation(s)) 
 
      
   
      
