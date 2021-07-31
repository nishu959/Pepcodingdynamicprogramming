n =int(input())

l = []

for i in range(n):
  a =list(map(int, input().split()))
  l.append(a)
 

red = l[0][0]
blue =l[0][1] 
green = l[0][2]


for i in l[1:]:
  
  nred = min(blue, green) + i[0]
  nblue = min(red, green) + i[1]
  ngreen = min(blue, red) + i[2]
  
  red = nred
  blue = nblue
  green = ngreen
  
  
  
  
print(min(red, blue, green))
  
  

