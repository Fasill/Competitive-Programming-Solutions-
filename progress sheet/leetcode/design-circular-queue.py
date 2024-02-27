class MyCircularQueue:

    def __init__(self, k: int):
        self.deque = deque([])    
        self.k = k    

    def enQueue(self, value: int) -> bool:
        if len(self.deque) <self.k:

            self.deque.appendleft(value)
            return True
        return False

    def deQueue(self) -> bool:
        if self.deque:

            self.deque.pop()
            return True
        return False

        

    def Front(self) -> int:
        if self.deque:

            return self.deque[-1]
        return -1
    def Rear(self) -> int:
        if self.deque:
            return self.deque[0]
        return -1
            

    def isEmpty(self) -> bool:
        if self.deque:
            return False
        return True

    def isFull(self) -> bool:
        if len(self.deque) == self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()