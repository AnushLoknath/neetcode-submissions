class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans={}
        for a,i in enumerate(numbers):
            diff=target-i
            if diff in ans:
                return [ans[diff]+1,a+1]
            ans[i]=a  
            

     
      
        

        