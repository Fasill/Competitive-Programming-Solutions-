class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
    
        stack = []
        hashSet = set()
        Counter = defaultdict(int)
        for i in range(len(s)):
            Counter[s[i]] = i
            
        n = len(s)
        
        for i in range(n):
            if s[i] not in hashSet :
                
                while stack and i < Counter[stack[-1]] and  stack[-1] > s[i] and  s[i] not in hashSet :
                    hashSet.discard(stack.pop())
                stack.append(s[i])
                hashSet.add(s[i])

        return "".join(stack)

                    

