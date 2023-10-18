#20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        if len(s)==1:
            return False
        for i in s:
            if not st:
                st.append(i)
            else:
                if st[-1]=='(' and i==')':
                    st.pop()
                elif st[-1]=='[' and i==']':
                    st.pop()
                elif st[-1]=='{' and i=='}':
                    st.pop()
                else:
                    st.append(i)
        if not st:
            return True
        return False
        