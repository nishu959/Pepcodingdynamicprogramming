n = int(input())
l = []

for i in range(n):
  l.append(int(input()))
  
maxprofit = 0
sd = 0
bd = 0


for i in range(1,n):
  
  if(l[i] > l[i-1]):
    sd += 1
    
  else:
    maxprofit += l[sd] - l[bd]
    sd = bd = i
    
    
maxprofit += l[sd] - l[bd] 
print(maxprofit)
  
  
   
    
  
  