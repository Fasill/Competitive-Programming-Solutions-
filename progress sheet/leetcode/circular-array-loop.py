class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def advance(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = advance(i)
            visited = set()

            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[advance(fast)] > 0:
                if slow == fast:
                    if slow == advance(slow):
                        break
                    return True

                visited.add(slow)

                slow = advance(slow)
                fast = advance(advance(fast))

                if slow in visited:
                    break

            slow = i
            while nums[slow] * nums[advance(slow)] > 0:
                next_slow = advance(slow)
                nums[slow] = 0
                slow = next_slow

        return False        