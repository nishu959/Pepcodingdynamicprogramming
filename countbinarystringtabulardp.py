n = int(input())

past = [[None for i in range(2)] for j in range(n+1)]


for i in range(1,n+1):
  for j in range(2):
    if(i==1):
      past[i][j] = 1
     
    else:
      if(j==0):
        past[i][j] = past[i-1][1]
         
      else:
        past[i][j] = past[i-1][1] + past[i-1][0]
         
     
print(past[n][1] +past[n][0])



