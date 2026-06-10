class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        gg= set()
        l=0
        ans=0

        for r in range(len(s)):
            while s[r] in gg:
                gg.remove(s[l])
                l+=1
            gg.add(s[r])
            ans= max(ans,r-l+1)
        return ans





    