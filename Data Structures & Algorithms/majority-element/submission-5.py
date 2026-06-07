class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        gg=Counter(nums)
        ans=gg.most_common(1)[0][0]
        return ans
       
   