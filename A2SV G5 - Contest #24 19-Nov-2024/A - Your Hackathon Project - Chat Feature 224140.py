# Problem: A - Your Hackathon Project - Chat Feature - https://codeforces.com/gym/534160/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    c = 0
    for i in range(n-1,-1,-1):
        if s[i] != ")":
            break
        c += 1
    if c <= n-c:
        print("NO")
    else:
        print("YES")