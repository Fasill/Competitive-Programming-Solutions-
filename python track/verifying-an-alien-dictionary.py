class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c: ix for ix, c in enumerate(order)}


        w = []
        for i in words:
            t = []
            for j in i:
                t.append(d[j])
            w.append(t)
        for i in range(1,len(w)):
            if w[i-1]>w[i]:
                return False
        return True
