class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long=0
        ans=set(nums)
        for i in ans:
            if i-1 not in ans:
                count=1
                while i+1 in ans:
                    i+=1
                    count+=1
                long=max(long,count)
            
        return long
       
            
    