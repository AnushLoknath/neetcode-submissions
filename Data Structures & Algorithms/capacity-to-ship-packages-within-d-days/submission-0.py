class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        ans=r

        def canship(cap):
            ships,currcap=1,cap
            for i in weights:
                if currcap - i<0:
                    ships+=1
                    if ships> days:
                        return False
                    currcap=cap 
                currcap-=i
            return True
        


        while l<=r:
            cap=(l+r) //2
            if canship(cap):
                ans=min(ans,cap)
                r=cap-1
            else:
                l=cap+1
        return ans
        

