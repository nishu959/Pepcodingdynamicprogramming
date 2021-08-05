
import sys

n = int(input())

l = []

for i in range(n):
  l.append(int(input()))
 
k = int(input())

dp = [[None for i in range(n)] for j in range(k+1)]

for i in range(k+1):
  for j in range(n):
    
    
    if(i==0 or j==0):
      
      dp[i][j] = 0
     
    else:
      
      mx = -1 * sys.maxsize 
      
      for q in range(j-1, -1,-1):
        
        diff = l[j] - l[q]
        mx = max(mx, dp[i-1][q] + diff)
       
      
      dp[i][j] = max(dp[i][j-1],mx)
    


print(dp[k][n-1])


