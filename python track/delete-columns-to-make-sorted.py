class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c = 0

        for i in range(len(strs[0])):
            st = []
            for j in strs:
                st.append(j[i])
            if st != sorted(st):
                c+=1
        return c 
