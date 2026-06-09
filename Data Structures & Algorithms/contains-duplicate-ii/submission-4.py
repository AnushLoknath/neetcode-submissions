class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        gg={}
        for a,i in enumerate(nums):
            if i in gg:
                if a-gg[i] <=k:
                    return True
            gg[i]=a
        return False
        






        
     


                    
                

         
        