class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        right,left = 0,0
        res = []
        s = 0
        for i in range(len(boxes)):
            if boxes[i] == "1":
                s+=i
                right +=1
        for i in range(len(boxes)):
            res.append(s)
            if boxes[i] == "1":
                right-=1
                left+=1
            s+=left
            s-=right
        return res