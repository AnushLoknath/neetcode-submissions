class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n = len(s1)

        if n > len(s2):
            return False

        s1Count = Counter(s1)

        for i in range(len(s2) - n + 1):
            if Counter(s2[i:i+n]) == s1Count:
                return True

        return False