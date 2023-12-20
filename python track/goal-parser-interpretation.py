class Solution(object):
    def interpret(self, command):
        ans = ""
        i=0
        while i < len(command):
            if command[i] == "(" and command[i+1] == ")":
                ans +="o"
                i+=2

            elif command[i] == "(" and command[i+1] == "a":
                ans+="al"
                i+=4
            else: 
                ans+="G"
                i+=1
        return ans
            



        return x