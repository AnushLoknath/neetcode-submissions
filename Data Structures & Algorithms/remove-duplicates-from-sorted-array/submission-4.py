class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans=[]
        gg=set()
        for i in nums:
            if i not in ans:
                ans.append(i)
            else:
                gg.add(i)
        for i in range(len(ans)):
            nums[i]=ans[i]
        return len(ans)

       