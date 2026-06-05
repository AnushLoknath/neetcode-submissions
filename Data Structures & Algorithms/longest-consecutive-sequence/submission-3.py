class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        gg=set(nums)
        long=0
        for i in gg:
            if i -1 not in gg:
                lenght=1
                while i+lenght in gg:
                    lenght+=1    
                long=max(long,lenght)  
        return long      


        
        