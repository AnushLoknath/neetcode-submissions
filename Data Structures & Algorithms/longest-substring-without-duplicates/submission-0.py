class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        gg=set()
        ans=0
        for i in range(len(s)):
            while s[i] in gg:
                gg.remove(s[left])
                left+=1
            gg.add(s[i])
            ans= max(ans,i-left+1)
        return ans 

        
        