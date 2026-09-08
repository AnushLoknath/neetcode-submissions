class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        gg={}
        for i,a in enumerate(nums):
            diff= target-a
            if diff in gg:
                return [gg[diff],i]
            gg[a]=i