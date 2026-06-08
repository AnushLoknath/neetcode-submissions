class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub=nums[0]
        gg=0
        for i in nums:
            if gg<0:
                gg=0
            gg+=i
            max_sub=max(max_sub,gg)
        return max_sub    







      

        