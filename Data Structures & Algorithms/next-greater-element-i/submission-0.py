class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        gg={}
        for i in nums2:
            while stack and i> stack[-1]:
                val=stack.pop()
                gg[val]=i
            stack.append(i)
        ans=[]
        for i in nums1:
            ans.append(gg.get(i,-1))
        return ans

