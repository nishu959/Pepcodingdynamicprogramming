
import sys

m, n = map(int, input().split())



l = []

for i in range(m):
  a =list(map(int, input().split()))
  l.append(a)



dp =[[None for i in range(n)] for j in range(m)]



for j in range(len(l[0])) :
  dp[0][j] = l[0][j]
 
#Two ways

for i in range(1,m):
  for j in range(n):
    
    minimum = sys.maxsize 
    for k in range(n):
      if(k!= j):
        minimum = min( dp[i-1][k], minimum)
    
    dp[i][j] = l[i][j] + minimum
    """
    if(j<n-1):
      
      dp[i][j] = l[i][j] + min(dp[i-1][:j] + dp[i-1][j+1:])
    else:
      dp[i][j] = l[i][j] + min(dp[i-1][:j])
    """


print(min(dp[m-1])) 
    
    