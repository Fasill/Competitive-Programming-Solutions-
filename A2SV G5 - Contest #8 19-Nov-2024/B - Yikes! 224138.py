# Problem: B - Yikes! - https://codeforces.com/gym/511242/problem/B

from bisect import * 
def f(n1,nums1,n2,num2):
    
    pre = [0]
    for i in range(n1):
        pre.append(pre[-1]+nums1[i])
    pre.pop(0)
    ans = []
    for i in range(n2):
        ans.append(bisect_left(pre,num2[i])+1)
    return ans
n1 = int(input())
nums1 = [int(i) for i in input().split()]
n2 = int(input())
nums2 = [int(i) for i in input().split()]
for num in f(n1,nums1,n2,nums2):
    print(num)