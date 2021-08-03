n = int(input())
l = []

for i in range(n):
  l.append(int(input()))



obsp = -1 * l[0]
ossp = 0
ocdp = 0


for i in range(1,n+1):
  
  nbsp = 0
  nssp = 0
  ncdp = 0
  
  if(ocdp-l[i-1] > obsp):
    nbsp = ocdp-l[i-1]    
  else:
    nbsp = obsp
  
  if(obsp+l[i-1] > ossp):
    nssp = obsp+l[i-1]    
  else:
    nssp = ossp
  
  if(ossp > ocdp):
    ncdp = ossp  
  else:
    ncdp  = ocdp
  
  obsp = nbsp 
  ossp = nssp 
  ocdp = ncdp 

print(ossp)

