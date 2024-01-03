class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        _hash = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                _hash[i+j].append(mat[i][j])
        ans = []
        for i in _hash:
            if i%2 == 0:
                for j in _hash[i][::-1]:
                    ans.append(j)
            else:
                for j in _hash[i]:
                    ans.append(j)
        return ans
        

                

