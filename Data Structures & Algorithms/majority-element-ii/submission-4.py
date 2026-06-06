class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        gg=Counter(nums)
        ans=[]
        for key,value in gg.items():
            if gg[key] > len(nums)//3:
                ans.append(key)
        return ans        


     