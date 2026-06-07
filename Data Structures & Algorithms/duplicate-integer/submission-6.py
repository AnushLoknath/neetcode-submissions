class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        gg=set()
        for i in nums:
            if i in gg:
                return True
            gg.add(i)  
        return False
              


     
