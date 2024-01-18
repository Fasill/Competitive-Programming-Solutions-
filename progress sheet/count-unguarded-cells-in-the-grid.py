class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        wall_set = set()
        for i in walls:
            wall_set.add((i[0],i[1]))
        guard_set = set()
        for i in guards:
            guard_set.add((i[0],i[1]))
        protected = set()
        for i in guards:
            x,y = i
            x +=1
            while x < m and (x,y) not in wall_set and (x,y) not in guard_set:
                protected.add((x,y))
                x+=1
            x,y = i
            x -=1
            while x >= 0 and (x,y) not in wall_set and (x,y) not in guard_set:
                protected.add((x,y))
                x-=1
            x,y = i
            y +=1
            while y < n and (x,y) not in wall_set and (x,y) not in guard_set:
                protected.add((x,y))
                y+=1
            x,y = i
            y -= 1
            while y>=0 and (x,y) not in wall_set and (x,y) not in guard_set:
                protected.add((x,y))
                y -= 1

        return (m*n-(len(wall_set)+len(guard_set)+len(protected)))        

