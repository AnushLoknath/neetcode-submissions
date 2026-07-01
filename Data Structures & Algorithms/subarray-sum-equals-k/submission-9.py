class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        gg={0:1}
        total=0
        count=0
        for i in range(len(nums)):
            total+=nums[i]
            need=total-k
            if need in gg:
                count+=gg[need]
            gg[total]=gg.get(total,0)+1
        return count

        