class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in s:
            if st:
                if i == "*":
                    st.pop()
                else:
                    st.append(i)

            else:
                if i != "*":
                    st.append(i)
        return "".join(st)