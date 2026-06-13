class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i,a in enumerate(temperatures):
            while stack and a> stack[-1][0]:
                stacka,stacki=stack.pop()
                ans[stacki]=i-stacki
            stack.append([a,i])
        return ans







        