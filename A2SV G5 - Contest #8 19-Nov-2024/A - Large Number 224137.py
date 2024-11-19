# Problem: A - Large Number - https://codeforces.com/gym/511242/problem/A

def f(d, num):
    
    _max = num + str(d)  
    for i in range(len(num)):
        if num[i] <str(d):
            _max = num[:i] +str(d) + num[i:]
            break
    return _max
 
 
for i in range(int(input())):
    n, d = map(int, input().split())
    num = input()
 
    result = f(d, num)
    print(result)