class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipR=s[l+1:r+1]
                skipL=s[l:r]
                return skipR==skipR[::-1] or skipL==skipL[::-1]
            else:
                l+=1
                r-=1    
        return True        

   