class TimeMap:

    def __init__(self):
        self.time_based = defaultdict(list)
       

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_based[key].append([timestamp,value])
     
        # self.li = sorted(self.li)

    def get(self, key: str, timestamp: int) -> str:
      
        ind = bisect_right(self.time_based[key],timestamp , key=lambda x:x[0])-1
        if ind>=len(self.time_based[key]):
            return ''
        if ind<0:
            return ''

        return self.time_based[key][ind][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
