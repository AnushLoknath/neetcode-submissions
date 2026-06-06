class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        gg=set(nums)
        long=0
        for i in gg:
            if i-1 not in gg:
                count=1
                while i+1 in gg:
                    i+=1
                    count+=1
                long=max(long,count)    
        return long             
       