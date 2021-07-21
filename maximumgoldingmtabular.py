import sys

m = int(input())
n = int(input())

l = []

for i in range(m):
  l.append(list(map(int, input().split())))

past = [[None for i in range(n)] for j in range(m)]


for j in range(len(l[0])-1,-1,-1):
  for i in range(len(l)-1, -1,-1):
   
    if(j==len(l[0])-1):
      past[i][j] = l[i][j]
     
    elif(i==0):
      past[i][j] =l[i][j] + max(past[i+1][j+1],past[i][j+1])
   
    elif(i==len(l)-1):
      
      past[i][j] =l[i][j] + max(past[i-1][j+1],past[i][j+1])
     
    else:
      past[i][j] =l[i][j] +max(past[i-1][j+1],past[i][j+1], past[i+1][j+1])

     
mx = -1*sys.maxsize   
for i in past:
  if(i[0] > mx):
    mx = i[0]   
    
print(mx)
  
  