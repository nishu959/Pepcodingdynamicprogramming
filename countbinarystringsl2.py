n =int(input())

oldzero = 1
oldone = 1

for i in range(2,n+1):
  nzero = oldone
  none = oldone + oldzero
  
  
  oldzero = nzero
  oldone = none 
  
 
print(nzero + none)
