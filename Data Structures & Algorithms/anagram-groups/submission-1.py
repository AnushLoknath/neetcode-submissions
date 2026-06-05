class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for i in strs:
            key="".join(sorted(i))
            if key not in group:
                group[key]=[i]
            else:
                group[key].append(i) 
        return(list(group.values()))       
         

               
         

 

