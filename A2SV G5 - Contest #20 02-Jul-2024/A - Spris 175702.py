# Problem: A - Spris - https://codeforces.com/gym/528792/problem/A

a = int(input())
b = int(input())
c = int(input())

if a <= 0:
    print(0)
else:
    _min= float("inf")
    _min = min(b// 2 ,_min)
    _min = min(c// 4 ,_min)
    _min = min(a,_min)
    print((_min * 1)+(_min * 2) + (_min * 4))
    
    
    
