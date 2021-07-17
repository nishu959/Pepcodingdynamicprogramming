import sys

n = int(input())

l = []

for i in range(n):
  l.append(int(input()))

dp = [None]*(n+1)

dp[n] = 0


for i in range(n-1,-1,-1):
  
  ans = sys.maxsize 
  
  for j in range(1,l[i]+1):
    
    if(i+j<=n and dp[i+j]!=None):
      ans = min(ans, dp[i+j]) 
  
  
  if(ans!= sys.maxsize):
    dp[i] = ans+1
    
  
  
print(dp[0])

