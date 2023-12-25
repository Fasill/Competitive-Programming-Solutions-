class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        c = 0

        for i in nums:
            if i % 2 == 0:
                c += i
        for i in queries:
            if nums[ i[-1]] % 2 == 0:
                c -= nums[ i[-1]]
            nums[ i[-1]] += i[0]
            if nums[ i[-1]] % 2 == 0:
                c += nums[ i[-1]]
            ans.append(c)
        return ans
