class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        p = []
        for i in path.split("/"):
            if i != "":
                p.append(i)

        for i in p:
            if st and i != ".":
                if i == "..":
                    st.pop()
                elif i == "/" and st[-1] == "/":
                    continue
                else:
                    st.append(i)
            
            else:
                if i not in {".",".."}:
                    st.append(i)
        return "/"+"/".join(st)
            