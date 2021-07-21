n = int(input())

past = [None]*(n+1)

for i in range(n,-1,-1):
  
  #this is optional
  if(i>n):
    pass
  
  if(i==n):
    past[i] = 1
  
  else:
    if(i+2>n):
      past[i] = past[i+1]
    elif(i+3>n):
      past[i] = past[i+1] + past[i+2]
    else:
      past[i] = past[i+1] + past[i+2]+ past[i+3]
      
      
    
 
 
print(past[0])  
    

  