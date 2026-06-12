class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        ans=set()
        total=0
        for i in range(len(s)):
            while s[i] in ans:
                ans.remove(s[l])
                l+=1
            ans.add(s[i])
            total=max(total,i-l+1)
        return total
  



    