class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        counter = 0
        for i in s:
            if stack:
                if i == ")" and stack[-1] not in {"(",")"}:
                    val = stack[-1]*2
                    stack.pop()
                    stack.pop()
                    while stack and stack[-1] not in {"(",")"}:
                        val += stack.pop()
                        
                    stack.append(val)
                elif i == ")" and stack[-1] in {"(",")"}:
                    stack.pop()
                    val = 1
                    while stack and stack[-1]  not in {"(",")"}:
                        val += stack.pop()

                    stack.append(val)
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return stack[0]
                
                
