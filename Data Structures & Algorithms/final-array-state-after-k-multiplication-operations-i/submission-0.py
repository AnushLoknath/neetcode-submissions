class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap,(nums[i],i))
        for i in range(k):
            val,n=heapq.heappop(heap)
            val=val*multiplier
            nums[n]=val
            heapq.heappush(heap,(val,n))
        return nums
        