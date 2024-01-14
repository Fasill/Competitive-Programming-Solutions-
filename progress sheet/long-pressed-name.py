class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name)>len(typed):
            return False
        i,j = 0,0
        while i<len(name) and j<len(typed):
            name_char = name[i]
            typed_char = typed[j]

            if name_char != typed_char:
                return False

            name_index = i+1
            typed_index = j+1

            while name_index<len(name) :
                if name[name_index-1] == name[name_index]:
                    name_index+=1
                else:break

            while typed_index < len(typed):
                if typed[typed_index - 1] == typed[ typed_index ]:
                    typed_index += 1
                else: break

            if name_index-i > typed_index-j:
                return False
            else:
                i,j = name_index,typed_index
        return i>=len(name) and j>=len(typed)


