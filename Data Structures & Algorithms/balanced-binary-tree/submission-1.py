
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True,0]
            left=dfs(node.left)
            right=dfs(node.right)
            blance=(left[0]and right[0] and abs(left[1]-right[1])<=1)
            height= 1+ max(left[1],right[1])
            return [blance,height]
        return dfs(root)[0]



        