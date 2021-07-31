s = input()

a = 0
ab = 0
abc = 0

for i in s:
  if(i=="a"):
    a = 2*a +1
  
  elif(i=="b"):
    ab = 2*ab + a
    
  elif(i=="c"):
    abc = 2*abc + ab
    
    
print(abc)


