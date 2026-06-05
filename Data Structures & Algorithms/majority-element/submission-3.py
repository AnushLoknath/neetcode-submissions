class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        gg=Counter(nums)
        output=gg.most_common(1)[0][0]
        return output
