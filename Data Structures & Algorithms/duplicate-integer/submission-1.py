class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashm = set()
        for i in nums:
            if i in hashm:
                return True
            hashm.add(i) 
        return False
               