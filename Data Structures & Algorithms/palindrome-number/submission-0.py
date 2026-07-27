class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev=0
        temp=x
        while temp:
            digit=temp%10
            rev=rev*10+int(digit)
            temp=temp//10
        if rev==x:
            return True
        return False
        