class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p1 = 0
        p2 = len(people)-1
        c = 0
        people = sorted(people)
        while p1<=p2:
            if people[p1]+people[p2] <= limit:
                p1+=1
                p2-=1
                c+=1
            elif people[p1]+people[p2] >= limit:
                p2 -= 1
                c += 1

        return c