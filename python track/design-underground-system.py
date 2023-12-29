class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.time = defaultdict(lambda: defaultdict(list))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation,t0 = self.checkin[id]
        self.time[startStation][stationName].append(t-t0)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t = self.time[startStation][endStation]
        av = sum(t)/len(t)
        return av


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)