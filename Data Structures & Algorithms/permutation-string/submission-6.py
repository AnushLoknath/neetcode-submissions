class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        if n>len(s2):
            return False
        s1count=Counter(s1)
        window=Counter(s2[:n])
        if s1count == window:
            return True
        for i in range(n,len(s2)):
            window[s2[i]]+=1
            window[s2[i-n]]-=1
            
            if s1count== window:
                return True
        return False





        

        

      
            
        
