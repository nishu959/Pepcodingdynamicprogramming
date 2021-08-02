import sys 

n = int(input())
l = []

for i in range(n):
  l.append(int(input()))
  

lsf = sys.maxsize 
pist = 0
maxprofit = 0


for i in l:
  if(i < lsf):
    lsf = i
   
  pist = i - lsf
  if(pist > maxprofit):
    maxprofit = pist
   
print(maxprofit)

