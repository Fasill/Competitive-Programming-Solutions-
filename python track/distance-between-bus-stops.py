class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            s = sum(distance[destination:start])
        else:
            s = sum(distance[start:destination])
        uq = sum(distance) - s
        return min(uq, s)

