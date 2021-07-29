p = input()
dp = [None for i in range(len(p)+1)]
p = p.strip() 


def numDecodings(s, dp):

    if len(s) == 0 or (len(s) == 1 and s[0] == '0'):
        return 0

    return numDecodingsHelper(s, len(s), dp)
 
 

def numDecodingsHelper(s, n, dp):
    if n == 0 or n == 1:
        dp[n] = 1
        return 1

    if(dp[n]!=None):
        return dp[n]
        
    count = 0
    
    if s[n-1] > "0":

        count = numDecodingsHelper(s, n-1, dp)

    if (s[n - 2] == '1' or (s[n - 2] == '2' and s[n - 1] < '7')):

        count += numDecodingsHelper(s, n - 2, dp)
    
    dp[n] = count

    return count
 
 
print(numDecodings(p, dp))