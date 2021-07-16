s = int(input())

def fibo(n, past):
  if(n==0 or n==1):
    return n
  
  if(past[n]!=-1):
    return past[n]
    
  
  p = fibo(n-1, past)
 
  q = fibo(n-2, past)
 
  ans = p + q
  past[n] = ans
 
  return ans
 
print(fibo(s, [-1]*(s+1)))

