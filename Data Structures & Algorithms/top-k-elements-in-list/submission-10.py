class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        gg=Counter(nums)
        heap=[]
        for num,count in gg.items():
            heapq.heappush(heap,(-count,num))
        ans=[]
        for i in range(k):
            count,num=heapq.heappop(heap)
            ans.append(num)
        return ans
        
        