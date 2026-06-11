
class Solution:
    def guessNumber(self, n: int) -> int:
        l=1
        r=n
        
        while l<=r:
            m=(l+r)//2
            ans=guess(m)
            if ans==0:
                return m
            elif ans==-1:
                r=m-1
            else:
                l= m+1



        




        