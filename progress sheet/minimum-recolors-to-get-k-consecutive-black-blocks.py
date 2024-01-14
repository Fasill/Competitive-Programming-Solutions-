class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l ,r= 0,k

        blocks = list(blocks)
        n = len(blocks)
        m = float('inf')
        while r<=n:
            w = blocks[l:r]
            m = min(m,w.count('W'))
            r+=1
            l+=1
        return m

