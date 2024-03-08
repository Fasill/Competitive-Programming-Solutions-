class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        li = []

        for i in range(len(houses)):
            br = bisect_right(heaters,houses[i])
            if br > len(heaters)-1:
                br-=1 
            if abs(heaters[br-1] - houses[i] )> abs(heaters[br] - houses[i]):
                    li.append(abs(heaters[br] - houses[i]))
            else:
                    li.append( abs(heaters[br-1] - houses[i]) )
        return max(li)       