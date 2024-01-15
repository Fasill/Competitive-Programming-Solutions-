class Solution:
    def minimumCardPickup(self, card: List[int]) -> int:
        d = {}
        _min = 10**6
        for i in range(len(card)):
            if card[i] in d:
                _min = min(_min,i-d[card[i]]+1)
            d[card[i]] = i
        if _min == 10**6:
            return -1
        return _min
