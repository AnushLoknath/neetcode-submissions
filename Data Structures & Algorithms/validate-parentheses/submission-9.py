class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        gg={")":"(","]":"[", "}":"{"}
        for i in s:
            if i in gg:
                if stack  and gg[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

        