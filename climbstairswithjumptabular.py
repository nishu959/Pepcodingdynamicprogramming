n =int(input())

l = []
for i in range(n):
  l.append(int(input()))
 

dp = [None]*(n+1)

dp[n] = 1

for i in range(n-1,-1,-1):
 
  ans = 0
  
  for j in range(1, l[i]+1):
    if(i+j<=n):
      ans += dp[i+j]
      
  dp[i] = ans
      
    
print(dp[0])
      
      
      
      
