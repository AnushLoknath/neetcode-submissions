class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[intervals[0]]
        for i in range(1,len(intervals)):
            current=intervals[i]
            last=ans[-1]
            if current[0]<=last[1]:
                last[1]=max(last[1],current[1])
            else:
                ans.append(current)
        return ans
            
        