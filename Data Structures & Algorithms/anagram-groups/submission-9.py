class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gg={}
        for i in strs:
            key="".join(sorted(i))
            if key not in gg:
                gg[key]=[i]
            else:
                gg[key].append(i)
        return list(gg.values())

        