class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        p1,p2 = 0,0
        _max = float("-inf")
        while p2<len(tasks):
            _max = max(_max,processorTime[p1]+tasks[p2])
            p1+=1
            p2+=4
        return _max
