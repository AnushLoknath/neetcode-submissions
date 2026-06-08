class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        gg=set()
        ans=[]
        for i in nums:
            if i in gg:
                ans.append(i)
            else:
                gg.add(i)
        return ans[0]            


        