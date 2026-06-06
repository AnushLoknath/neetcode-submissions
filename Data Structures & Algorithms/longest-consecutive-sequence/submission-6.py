class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        gg=set(nums)
        long=0
        for i in nums:
            if i -1 not in gg:
                length=1
                while i+ length in gg:
                    length+=1
                long=max(long,length)
        return long        
