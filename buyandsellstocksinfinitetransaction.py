
n = int(input())
l = []

for i in range(n):
  l.append(int(input()))
  
maxprofit = 0

for i in range(1,n):
  if(l[i]>l[i-1]):
    maxprofit += l[i]-l[i-1]
    
 
print(maxprofit)
    