class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for i in strs:
            Key ="".join(sorted(i))
            if Key not in group:
                group[Key]=[i]
            else:
                group[Key].append(i)    
            
        return list(group.values())  


               
         

 

