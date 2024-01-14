class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        n,m = len(players),len(trainers)
        i,j = 0,0
        c = 0
        players.sort()
        trainers.sort()
        while i<n:

            while j<len(trainers):
                if players[i]<=trainers[j]:
                    c+=1
                    j+=1
                    break
                else:
                    j+=1
            
            i+=1
        return c
