class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        plants.insert(0,capacity)
        lake=0
        can=1
        cap=plants[lake]
        count=0
        while can<len(plants):
            if cap>=plants[can]:
                count+=1
                cap-=plants[can]
                can+=1
            else:
                count+=(can-1)*2
                cap=plants[lake]
        return count