class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        m = {')':'(',']':'[','}':"{"}
        stack = []
        for i in s:
            if i in m:
                if not stack or stack.pop()!= m[i]:
                    return False
            else:
                stack.append(i)
        
        return not stack



        