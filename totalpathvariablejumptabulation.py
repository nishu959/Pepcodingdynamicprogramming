n =int(input())

l = []
for i in range(n):
  l.append(int(input()))
 

past = [None]*(n+1)

for i in range(n, -1,-1):
  
  if(i==n):
    past[i] = 1
    
  else:
    
    ans = 0
    
    for j in range(1,l[i]+1):
      if(i+j<=n):
        ans += past[i+j]
        
    past[i] = ans
 
 
print(past[0]) 

