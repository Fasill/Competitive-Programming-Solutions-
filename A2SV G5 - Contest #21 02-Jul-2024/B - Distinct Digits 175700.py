# Problem: B - Distinct Digits - https://codeforces.com/gym/530187/problem/B


t = int(input())
for _ in range(t):
    n = int(input())   
    
    def dp(i,tot):
        if tot == n:
            return str(i)
        ans = "999999999"
        for j in range(i + 1,10):
            if tot + j <= n:
                ans = min(int(ans),int(str(i) + dp(j,tot + j)))            
            
        return str(ans)
    
    print(dp(0,0))