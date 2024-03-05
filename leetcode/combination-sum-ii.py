class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        self.cur = []
        ref = set()

        counter = Counter(candidates)
        uniqueNumbers = list(set(candidates))
        uniqueNumbers.sort()
        n = len(uniqueNumbers)

        def dfs(i=0,total=0):
            cur = self.cur
            if total == target:
                _tuple = tuple(cur[:])
                if _tuple not in ref:

                    combs.append(cur[:])
                    ref.add(_tuple)
                return

            if i >= n or total > target:
                return
            for j in range(i,n):
                cur.append(uniqueNumbers[j])
                
                if counter[uniqueNumbers[j]] > 1:
                    counter[uniqueNumbers[j]] -= 1
                    dfs(j,total+uniqueNumbers[j])
                    cur.pop()
                    counter[uniqueNumbers[j]] += 1
                else:
                    # counter[uniqueNumbers[j]] -= 1

                    dfs(j+1,total+uniqueNumbers[j])
                    cur.pop()
                    # counter[uniqueNumbers[j]] += 1


        dfs()
        return combs