class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         final_res= None
         count= 0
         for num in nums:
            if count==0:
                final_res=num
            if num== final_res:
                count+=1
            else:
                count-=1
         return final_res           

