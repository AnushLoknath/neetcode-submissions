class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        gg={}
        for i,a  in enumerate(numbers):
            diff= target-a
            if diff in gg:
                return [gg[diff]+1,i+1]
            gg[a]=i      