n = int(input())

past = [None]*(n+1)

for i in range(n,-1,-1):
  
  #this is optional
  if(i>n):
    pass
  
  if(i==n):
    past[i] = 1
  
  else:
    
    ans = 0
    
    for j in range(1,4):
      
      if(i+j<=n):
        ans += past[i+j]
     
    past[i] = ans   
    
 
 
print(past[0])  
    

  