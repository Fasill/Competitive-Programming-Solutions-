from math import *
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ans =  abs(target[0])+abs(target[1])
        for i in ghosts:
            if ans >=abs(i[0]-target[0])+abs(i[1]-target[1]):
                return False 
        return True 
