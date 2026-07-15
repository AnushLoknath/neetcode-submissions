class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        gg={}
        for a,i in enumerate(nums):
            diff=target-i
            if diff in gg:
                return[gg[diff],a]
            gg[i]=a
        