n = int(input())
l = []

for i in range(n):
  l.append(int(input()))
 
 

class buyandsell():
  def __init__(self, buy, sell, cooldown):
    self.buy = buy
    self.sell = sell
    self.cooldown = cooldown 
  

def buysell(m):
  if(m==0):
    a = buyandsell(-l[0],0, 0)
    return a
   
  a = buysell(m-1)
  
  
  p1 = max(a.cooldown - l[m-1],a.buy)
  p2 = max(a.buy + l[m-1], a.sell)
  p3 = max(a.sell, a.cooldown)
  
  p = buyandsell(p1,p2, p3)
  
  
  return p
  
print(buysell(n).sell)

 