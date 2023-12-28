class Solution:
    def printVertically(self, s: str) -> List[str]:
        strings = []
        d = s.split()
        m = 0
        for i in d:
            strings.append(list(i))
            m = max(len(i),m)

        ans = []
        for i in range(m):
            t = []
            for j in strings:
                if len(j) > i:
                    t.append(j[i])
                else:t.append(" ")
            ans.append("".join(t).rstrip())
        return ans

            



