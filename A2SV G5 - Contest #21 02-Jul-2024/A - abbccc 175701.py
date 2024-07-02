# Problem: A - abbccc - https://codeforces.com/gym/530187/problem/A

t = int(input())
s = input()

res = []
i = 0
c = 0
while i < t:
    res.append(s[i])
    
    c += 1
    i += c
print("".join(res))