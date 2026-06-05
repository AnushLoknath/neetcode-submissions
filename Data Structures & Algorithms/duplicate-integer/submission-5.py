class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        gg=set()
        for i in nums:
            if i not in gg:
                gg.add(i)
            else:     
                return True
        return False        

