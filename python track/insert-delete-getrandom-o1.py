class RandomizedSet:

    def __init__(self):
        self.RandomizedSet = []
    def insert(self, val: int) -> bool:
        RandomizedSet = self.RandomizedSet
        if val not in RandomizedSet:
            RandomizedSet.append(val)
            return True
        else: return False

    def remove(self, val: int) -> bool:
        RandomizedSet = self.RandomizedSet
        if val not in RandomizedSet:
            return False
        else: 
            RandomizedSet.remove(val)
            return True

    def getRandom(self) -> int:
        RandomizedSet = self.RandomizedSet

        return random.choice(RandomizedSet)


        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()