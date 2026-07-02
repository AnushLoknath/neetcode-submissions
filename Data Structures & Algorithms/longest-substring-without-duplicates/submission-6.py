class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        gg=set()
        ans=0
        l=0

        for i in range(len(s)):
            while s[i] in gg:
                gg.remove(s[l])
                l+=1
            gg.add(s[i])
            ans= max(ans,i-l+1)
        return ans

                

        