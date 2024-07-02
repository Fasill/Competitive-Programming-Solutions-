# Problem: A - The Coordinate Challenge - https://codeforces.com/gym/531455/problem/A

t = int(input())
for _ in range(t):
    num = int(input()) 
    if num == 1:
        print(2)
    else:
        print((num+2) //3)
