import sys 

n =int(input())

past = [None]*(n+1)

l = []
for i in range(n):
  l.append(int(input()))
  
  
for i in range(n, -1,-1):
  
  if(i==len(l)):
    past[i] = 0
  
  else:
    
    ans = sys.maxsize 
    for j in range(1,l[i]+1):
      if(i+j<=len(l)):
        ans = min(ans, past[i+j])
    
    past[i] = ans + 1
    
    
print(past[0])
   
  
  
 
