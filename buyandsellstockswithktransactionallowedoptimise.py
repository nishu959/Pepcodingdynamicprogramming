
import sys

n = int(input())

l = []

for i in range(n):
  l.append(int(input()))
 
k = int(input())

dp = [[None for i in range(n)] for j in range(k+1)]

for i in range(k+1):
  
  mx = -1 * sys.maxsize
  
  for j in range(n):
    
    
    if(i==0 or j==0):
      
      dp[i][j] = 0
     
    else:
      
      if(dp[i-1][j-1] - l[j-1] > mx):
        mx = dp[i-1][j-1] - l[j-1]
       
      
      
      #here l[j] part remains same in every 
      #iteration so we need to calculate
      #max for the variable part only
      
      dp[i][j] = max(dp[i][j-1],mx + l[j])
    


print(dp[k][n-1])


