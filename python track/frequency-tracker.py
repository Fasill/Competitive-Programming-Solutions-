class FrequencyTracker:

    def __init__(self):
        self.cnter, self.freq = defaultdict(int), defaultdict(int)
        
    def add(self, number: int) -> None:
        self.cnter[number] += 1
        self.freq[cnt := self.cnter[number]] += 1
        self.freq[cnt-1] -= 1
        
    def deleteOne(self, number: int) -> None:
        if self.cnter[number]:
            self.cnter[number] -= 1
            self.freq[cnt := self.cnter[number]] += 1
            self.freq[cnt+1] -= 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
