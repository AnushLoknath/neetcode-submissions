class Solution:
    def isPalindrome(self, s: str) -> bool:
        gg=""
        for i in s:
            if i.isalnum():
                gg+=i.lower()
        return gg==gg[::-1]    
       




       