class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        '''
            sort = O(nlogn)
            len = O(n)
            loop = O(n)
            overall = O(nlogn)
        '''
        s = sorted(piles,reverse=True)

        n = (len(piles)//3)
        ans= 0
        for i in range(1,n*2,2):
            ans += s[i]
            print(s[i])
        print(s)

        return ans

