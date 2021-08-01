n =int(input())
m = int(input())


if(m>n):
  print(1)
  
else:
  dp = [None for i in range(n+1)]

  for i in range(m):
    dp[i] = 1


  dp[m] = 2




  for i in range(m+1,n+1):
    dp[i] = dp[i-1] + dp[i-m]



  print(dp[n]) 

