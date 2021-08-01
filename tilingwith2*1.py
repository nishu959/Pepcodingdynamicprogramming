n = int(input())

hz = 0
vt = 1
#hz = 1,vt = 1 also work
#in that case lopp starts from 3

for i in range(2,n+1):
  nhz = vt
  nvt = hz + vt
  
  hz = nhz
  vt = nvt
  
  
  
print(hz+vt)
  
  