class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        daily_amount = 1
        
        for day in range(1, n + 1):
            total += daily_amount
            daily_amount += 1

            if day % 7 == 0:
                daily_amount = day // 7 + 1

        return total