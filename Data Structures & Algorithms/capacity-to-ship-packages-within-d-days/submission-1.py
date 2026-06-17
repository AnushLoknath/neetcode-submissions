class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        ans=r

        def gg(m):
            ship,currm=1,m
            for i in weights:
                if currm -i<0:
                    ship+=1
                    currm=m
                currm -=i
            return ship<= days

        while l<=r:
            m=(l+r)//2
            if gg(m):
                ans=m
                r=m-1
            else:
                l=m+1
        return ans
            
                   

                 

        

