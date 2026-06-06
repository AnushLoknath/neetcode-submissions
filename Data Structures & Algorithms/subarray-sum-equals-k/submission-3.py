class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total=0
        count=0
        gg={0:1}
        for i in nums:
            total+=i
            need=total-k
            if need in gg:
                count+=gg[need]
            gg[total]=gg.get(total,0)+1
        return count        


