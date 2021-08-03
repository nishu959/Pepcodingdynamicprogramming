import sys 

n = int(input())
l = []

for i in range(n):
  l.append(int(input()))
  
  
  
dp1 = [None]*(n) 
dp1[0] = 0

lsf = sys.maxsize 
maxproleft = 0
  
for i in range(1,n):
  if(l[i] <lsf):
    lsf = l[i]
 
  pro = l[i] - lsf
  if(pro > maxproleft):
    dp1[i] = pro
    maxproleft  = pro
    
  else:
    dp1[i] = maxproleft
    
 
 
 
    
dp2 = [None]*(n) 
dp2[n-1] = 0

msf = -1*sys.maxsize 
maxproright = 0
  
for i in range(n-1,-1,-1):
  if(l[i] >msf):
    msf = l[i]
 
  pro = msf - l[i]
  if(pro > maxproright):
    dp2[i] = pro
    maxproright  = pro
    
  else:
    dp2[i] = maxproright
    
    
    

ans = -1 * sys.maxsize   

for i in range(n):
  
  if(dp1[i]+dp2[i] > ans):
    ans = dp1[i]+dp2[i]
    
    
print(ans)
  
    
    

   
  