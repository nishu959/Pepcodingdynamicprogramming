m = int(input())
n = int(input())


if(n>m or m==0 or n==0):
  print(0)
  
 
dp = [[None for i in range(n+1)]for j in range(m+1)]


for p in range(0,m+1):
  for t in range(0,n+1):
    
    if(p==0 or t==0):
      dp[p][t] = 0
   
    if(t==p):
      dp[p][t] = 1
      
     
    elif(t==1):
      dp[p][t] = 1
    
    
    elif(t>p):
      dp[p][t] = 0
     
    else:
      dp[p][t] = dp[p-1][t-1] + t* dp[p-1][t]
     
    
print(dp[m][n])

