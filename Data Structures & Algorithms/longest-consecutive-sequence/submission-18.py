class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        gg=set(nums)
        longt=0
        for i in gg:
            if i-1 not in gg:
                count=1
                while i+1 in gg:
                    count+=1
                    i+=1
                longt=max(longt,count)
        return longt
