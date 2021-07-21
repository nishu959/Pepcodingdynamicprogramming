n =int(input())

past = [None]*(n+1)

for i in range(n+1):
  if(i==0 or i==1):
    past[i] = i
 
  else:  
    a = past[i-1] 
    b = past[i-2]
    ans = a + b
    
    past[i] = ans


print(past[n])