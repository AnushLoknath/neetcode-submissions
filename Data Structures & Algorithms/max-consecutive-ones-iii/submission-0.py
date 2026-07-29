class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans=0
        count=0
        l=0

        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            while count> k:
                if nums[l]== 0:
                    count-=1
                l+=1
            ans=max(ans,i-l+1)
        return ans

        