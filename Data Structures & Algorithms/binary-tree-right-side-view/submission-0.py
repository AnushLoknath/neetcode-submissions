
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        q=collections.deque()
        q.append(root)
        while q:
            qlen=len(q)
            level=[]
            for i in range(qlen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                ans.append(level[-1])
        return ans


        
        
        


        
        