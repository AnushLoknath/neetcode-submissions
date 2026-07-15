class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        gg=s.split()
        return len(gg[-1])

        