class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        gg=[]
        ans=Counter(nums)
        for i in ans.most_common(k):
            index=i[0]
            gg.append(index)
        return gg


