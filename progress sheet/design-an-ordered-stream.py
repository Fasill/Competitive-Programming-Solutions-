class OrderedStream:

    def __init__(self, n: int):
        self.li = [0]*n
        self.p = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.li[idKey-1]=value
        res = []
        for i in range( self.p,len(self.li)):
            if self.li[i] == 0:
                break
            self.p+=1
            res.append(self.li[i])
        return res 



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)