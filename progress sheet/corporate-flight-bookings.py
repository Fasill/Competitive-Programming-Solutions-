class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prifix = [0 for i in range(1,n+1)]

        for booking in bookings:
            prifix[booking[0]-1] += booking[-1]
            if booking[1] != n:
                prifix[booking[1]] -= booking[-1]
        
        for i in range(1,len(prifix)):
            prifix[i] += prifix[i-1]
        return prifix
