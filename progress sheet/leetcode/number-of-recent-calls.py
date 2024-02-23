class RecentCounter:

    def __init__(self):
        self.q=deque()

    def ping(self, t: int) -> int:
        q = self.q
        q.append(t)
        _range = t-3000
        while q[0]<_range:
            q.popleft()
            
        return len(q) 

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)