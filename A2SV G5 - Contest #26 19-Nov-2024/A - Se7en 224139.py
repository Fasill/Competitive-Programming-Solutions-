# Problem: A - Se7en - https://codeforces.com/gym/537362/problem/A


def make_divisible_by_7(num_str):
    num = int(num_str)
    if num % 7 == 0:
        return num_str
    
    for i in range(len(num_str)):
        for digit in '0123456789':
            if i == 0 and digit == '0':
                continue
            new_num_str = num_str[:i] + digit + num_str[i+1:]
            if int(new_num_str) % 7 == 0:
                return new_num_str
    
    return num_str

t = int(input())
for _ in range(t):
    num_str = input().strip()
    print(make_divisible_by_7(num_str))

