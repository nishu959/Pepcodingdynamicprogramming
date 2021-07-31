n =int(input())
l = []

for i in range(n):
  l.append(int(input()))
  
  
inc = l[0]
exc = 0

for i in l[1:]:
  ninc = exc + i
  nexc = max(inc, exc)
 
  inc = ninc
  exc = nexc
 

print(max(inc, exc))

