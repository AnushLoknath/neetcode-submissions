class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        gg={}
        for a,i in enumerate(numbers):
            diff= target-i
            if diff in gg:
                return[gg[diff]+1,a+1]
            gg[i]=a


        
       
       
     
      
        

        