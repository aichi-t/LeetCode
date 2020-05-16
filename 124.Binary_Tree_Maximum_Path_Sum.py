import sys
sys.path.append("../algo_ds/Tree")
from Tree import Tree

class Solution:
    current_max = float("-inf")
    def maxPathSum(self,root):
        self.helper(root)
        return self.current_max

    def helper(self,node):
        if node is None:
            return node 
        left = self.helper(node.left)
        right = self.helper(node.right)
        left = 0 if left is None else (left if left > 0 else 0)
        right = 0 if right is None else (right if right > 0 else 0)
        self.current_max = max(left+right+node.val,self.current_max)
        return max(left,right) + node.val

if __name__ == "__main__":
    # nodes = [1,2,3]
    nodes = [-10,9,20,None,None,15,7]
    tree = Tree(nodes)
    s = Solution()
    print(s.maxPathSum(tree.root))

    