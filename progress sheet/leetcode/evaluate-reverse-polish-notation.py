class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        x = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                x.append(int(x.pop() + x.pop()))

            elif tokens[i] == '*':
                x.append(int(x.pop() * x.pop()))

            elif tokens[i] == '-':
                operand2 = x.pop()
                operand1 = x.pop()
                result = operand1 - operand2
                x.append(int(result))

            elif tokens[i] == '/':
                operand2 = x.pop()
                operand1 = x.pop()
                result = operand1 / operand2
                x.append(int(result))

            else:
                x.append(int(tokens[i]))
        return int(x[0])