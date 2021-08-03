n = int(input())
l = []

for i in range(n):
  l.append(int(input()))
 
 
fee = int(input())

class buyandsell():
  def __init__(self, buy, sell):
    self.buy = buy
    self.sell = sell
  

def buysell(m):
  if(m==0):
    a = buyandsell(-l[0],0)
    return a
   
  a = buysell(m-1)
  
  
  p1 = max(a.sell- l[m-1],a.buy)
  p2 = max(a.buy + l[m-1] - fee, a.sell)
  
  p = buyandsell(p1,p2)
  
  
  return p
  
print(buysell(n).sell)

