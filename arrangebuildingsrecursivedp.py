n = int(input())


past = [[None for i in range(2)] for j in range(n+1)]

def arrbuild(n, place, past):
  if(n==1):
    past[n][place] = 1
    return 1
    
   
  if(past[n][place]!=None):
    return past[n][place]
  
  
  
  if(place == 0):
    ans = arrbuild(n-1, 1, past)
    past[n][place] = ans
    return ans
    
  else:
    ans1 =arrbuild(n-1, 0, past)
    ans2 =arrbuild(n-1, 1, past)
    ans = ans1 + ans2 
    past[n][place] = ans
    return ans
    
#0 for house
#1 for space

p = arrbuild(n, 0, past) + arrbuild(n, 1, past)
    
    
print(p**2)
