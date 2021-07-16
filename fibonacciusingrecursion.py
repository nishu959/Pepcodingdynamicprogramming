s = int(input())

def fibo(n):
  if(n==0 or n==1):
    return n
   
  p = fibo(n-1)
 
  q = fibo(n-2)
 
  ans = p + q
 
  return ans
 
print(fibo(s))

