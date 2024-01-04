class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        l = 0
        r = len(skill)-1
        skill = sorted(skill)
        s1 = 0
        s2 = sum(skill)

        sums = skill[l]+skill[r]
        ans = []
        while l<r:
            if skill[l]+skill[r] == sums:
                ans.append(skill[l]*skill[r] )
                s1+=(skill[l]+skill[r])

                l+=1
                r-=1
            elif  skill[l]+skill[r] < sums:
                l+=1

            elif  skill[l]+skill[r] > sums:
                r -=1
        if s2  != s1:
            return -1
        return sum(ans)




