n = int(input())

past = [[None for i in range(2)] for j in range(n+1)]

def countbinary(n, pre):
  if(n==0):
    past[n][pre] = 1
    return 1
 
  
  if(past[n][pre]!=None):
    return past[n][pre]
 
  
  if(pre == 0):
    ans1 = countbinary(n-1, 1)
    past[n][pre] = ans1
    
    return ans1
  else:
    ans3 = countbinary(n-1, 1)
    ans4 = countbinary(n-1, 0) 
    ans2 = ans3 + ans4
    past[n][pre] = ans2
    
    return ans2
   
    
    

ans = countbinary(n-1, 1)+countbinary(n-1, 0)
print(ans)

