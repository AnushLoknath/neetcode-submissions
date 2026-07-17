class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap=[]
        for i in gifts:
            heapq.heappush(heap,-i)
        for i in range(k):
            n=-heapq.heappop(heap)
            heapq.heappush(heap,-int(sqrt(n)))
        return -sum(heap)

        
        