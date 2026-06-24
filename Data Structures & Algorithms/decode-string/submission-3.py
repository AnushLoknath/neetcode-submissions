class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i !="]":
                stack.append(i)
            else:
                gg=""
                while stack and stack[-1]!="[":
                    gg=stack.pop()+gg
                stack.pop()

                k=""
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k
                stack.append(gg*int(k))
        return "".join(stack)



            
       
            