import sys

m = int(input())
n = int(input())

l = []

for i in range(m):
  l.append(list(map(int, input().split())))

past = [[None for i in range(n)] for j in range(m)]

def goldmine(l, m, n, past):
  
  if(m<0 or m>=len(l)):
    
    return -1*sys.maxsize 
     
  
  if(n==len(l[0])-1):#if(n==len(l[0])):return 0
    past[m][n] = l[m][n]
    return l[m][n]
    
   
  if(past[m][n]!=None):
    return past[m][n]
    
    
  a = goldmine(l, m-1, n+1, past)
  b = goldmine(l, m, n+1, past)
  c = goldmine(l, m+1, n+1, past)
  
   
  ans = max(a, b, c) + l[m][n]
  past[m][n] = ans
  
  return ans
  



mg = 0
for i in range(m):
  p = goldmine(l, i, 0, past)
  if(p>mg):
    mg = p
   
print(mg)
