import sys
sys.path.append("../algo_ds/Tree")
from Tree import Tree

class Solution:
    # def maxDepth(self,root):
    #     return self.bfs(root,1)
    
    def bfs(self,node,level):
        if not node:
            return level -1
        else:
            return max(self.bfs(node.left,level+1),self.bfs(node.right,level+1))
        
    # def maxDepth(self,root):
    #     return 1 + max(map(self.maxDepth,(root.left,root.right))) if root else 0

if __name__ == "__main__":
    nodes = [3,9,20,None,None,15,7]
    # nodes = [None]
    tree = Tree(nodes)
    s = Solution()
    print(s.maxDepth(tree.root))