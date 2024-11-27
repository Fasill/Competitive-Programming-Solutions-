# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

n,m,q=list(map(int,input().split()))
 
 
rank = [0] * (n + 1)
parent = list(range(n + 1))
size = [1] * (n + 1)
count = n
 
def find(node):
    if node == parent[node]:
        return node
 
    stack = []
    while node != parent[node]:
        stack.append(node)
        node = parent[node]
 
    # Path compression
    for n in stack:
        parent[n] = node
 
    return node
 
def Runion(u, v):
    rep_u = find(u)
    rep_v = find(v)
    if rep_u == rep_v:
        return False
    if rank[rep_u] < rank[rep_v]:
        parent[rep_u] = rep_v
    elif rank[rep_v] < rank[rep_u]:
        parent[rep_v] = rep_u
    else:
        parent[rep_v] = rep_u
        rank[rep_u] += 1
 
    return True
 
    # def Sunion(self, u, v):
    #     rep_u = self.find(u)
    #     rep_v = self.find(v)
    #     if rep_u == rep_v:
    #         return
    #     if self.size[rep_u] < self.size[rep_v]:
    #         self.parent[rep_u] = rep_v
    #         self.size[rep_v] += self.size[rep_u]
    #     else:
    #         self.parent[rep_v] = rep_u
    #         self.size[rep_u] += self.size[rep_v]
 
import sys
def inputt():
    return sys.stdin.readline().strip()
def printt(output):
    return sys.stdout.write(str(output)+"\n")
def longInput():
    return [int(i) for i in inputt().split()]
 
li=[]
for _ in range(m):
    li.append(tuple(map(int,input().split())))
request=[]
# dsu = DSU(n)
for _ in range(q):
    request.append(input().split())
results=[]
for query,u,v in reversed(request):
    u,v=int(u),int(v)
    if query!="ask":
        Runion(u,v)
    else:
        if find(u)==find(v):
            results.append("YES")
        else:
            results.append("NO")
for result in reversed(results):
    print(result)