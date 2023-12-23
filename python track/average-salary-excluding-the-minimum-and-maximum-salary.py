class Solution:
    def average(self, salary: List[int]) -> float:
        x = max(salary)
        
        it = salary.count(x)
        for i in range(it):
            salary.remove(x)
        y = min(salary)
        mi = salary.count(y)

        for i in range(mi):
            salary.remove(y)

        s = sum(salary)
        return s/len(salary)
        