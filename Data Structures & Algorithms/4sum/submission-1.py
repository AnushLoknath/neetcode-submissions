class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        for a in range(len(nums)):
            if a>0 and nums[a]== nums[a-1]:
                continue
            for b in range(a+1,len(nums)):
                if b>a+1 and nums[b]== nums[b-1]:
                    continue
                l=b+1
                r=len(nums)-1
                while l<r:
                    forsum=nums[a]+nums[b]+nums[l]+nums[r]
                    if forsum>target:
                        r-=1
                    elif forsum<target:
                        l+=1
                    else:
                        ans.append([nums[a],nums[b],nums[l],nums[r]])
                        l+=1
                        while l<r and nums[l]== nums[l-1]:
                            l+=1
        return ans     


       
        