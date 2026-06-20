class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows,col=len(matrix),len(matrix[0])
        ans=[[0]*rows for i in range(col)]
        for r in range(rows):
            for c in range(col):
                ans[c][r]=matrix[r][c]
        return ans

        