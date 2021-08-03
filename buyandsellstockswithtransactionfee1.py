n = int(input())
l = []

for i in range(n):
  l.append(int(input()))
 
 
fee = int(input())


obsp = -l[0]
ossp = 0

for i in range(1,n):
  nbsp = 0
  nssp = 0
  
  if(ossp - l[i] > obsp):
    nbsp = ossp - l[i] 
  else:
    nbsp = obsp
    
  
  if(obsp + l[i] - fee > ossp):
    nssp = obsp + l[i] - fee
  else:
    nssp = ossp
    
  obsp = nbsp
  ossp = nssp
    
    
print(nssp)
    