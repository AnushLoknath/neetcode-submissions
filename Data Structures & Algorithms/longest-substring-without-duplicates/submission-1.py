class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        ans=set()
        total=0
        for r in range(len(s)):
            while s[r] in ans:
                ans.remove(s[l])
                l+=1
            ans.add(s[r])
            total=max(total,r-l+1)
        return total
                

       