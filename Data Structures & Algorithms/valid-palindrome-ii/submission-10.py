class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        for i in range(len(s)):
            if s[l]!=s[r]:
                skipl=s[l+1:r+1]
                skipr=s[l:r]
                return skipr == skipr[::-1] or skipl==skipl[::-1]
            l+=1
            r-=1
        return True    


      
            

        


       