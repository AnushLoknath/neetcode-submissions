class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count={}
        ans=0
        l=0
        for i in range(len(fruits)):
            count[fruits[i]]=count.get(fruits[i],0)+1
            while len(count)>2:
                count[fruits[l]]-=1
                if count[fruits[l]]==0:
                    del count[fruits[l]]
                l+=1
            ans=max(ans,i-l+1)
        return ans
        