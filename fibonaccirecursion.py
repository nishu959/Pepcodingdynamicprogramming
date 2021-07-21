n = int(input())

def fibo(n):
  if(n==0 or n==1):
    return n
   
  a = fibo(n-1)

  b = fibo(n-2)
  
  ans = a + b
  
  return ans
 
  
print(fibo(n))
  