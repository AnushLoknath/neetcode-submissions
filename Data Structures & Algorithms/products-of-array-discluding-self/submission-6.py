class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final=[1]*len(nums)
        pre=1
        for i in range(len(nums)):
            final[i]=pre
            pre*=nums[i]
        sufix=1
        for i in range(len(nums)-1,-1,-1):
            final[i]*=sufix
            sufix*=nums[i]
        return final        


           


       
            

            
        