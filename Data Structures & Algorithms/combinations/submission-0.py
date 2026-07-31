class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        sol = []
        def backtrack(i):
            if len(sol) == k:
                ans.append(sol[:])
                return 
            for i in range(i,n+1):
                sol.append(i)
                backtrack(i+1)
                sol.pop()
        backtrack(1)
        return ans

        