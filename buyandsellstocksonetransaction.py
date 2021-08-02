import sys 

n = int(input())
l = []

for i in range(n):
  l.append(int(input()))
  
  
mininarr = l[0]

maxprofit = -sys.maxsize 


for i in l[1:]:
  pro = i - mininarr
  if(pro > maxprofit):
    maxprofit  = pro
    
  mininarr = min(mininarr, i)
  
  
print(maxprofit)
