class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        for i, num in enumerate(nums):
            ans = target - num
            if ans in hashm:
                return [hashm[ans], i]
            hashm[num] = i

        return [-1, -1]
