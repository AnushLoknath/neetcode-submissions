class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num={}
        for a,i in enumerate(nums):
            diff= target-i
            if diff in num:
                return[num[diff],a]
            num[i]=a    
   




     