class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextMaxEelemnts = []
        hm = defaultdict(int)
        for i in nums2[::-1]:
            while stack and stack[-1]<i:
                stack.pop()
            if not stack:
                hm[i] = -1
            else:
                hm[i] = stack[-1]
            stack.append(i)

        return [hm[i] for i in nums1 ]