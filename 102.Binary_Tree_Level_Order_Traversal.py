import sys
sys.path.append("../algo_ds/Tree")

from Tree import Tree

class Solution:
    def levelOrder(self, root):
        visited = []
        self.dfs(root,visited,0)
        return visited

    def dfs(self,node,visited,depth):
        if node is None:
            return
        if len(visited) <= depth:
            visited.append([])
        visited[depth].append(node.val)
        self.dfs(node.left,visited,depth+1)
        self.dfs(node.right,visited,depth+1)





if __name__ == "__main__":
    # nodes = [3, 9, 20, None, None, 15, 7]
    nodes = [1,2,3,4,5,6,7,8]
    tree = Tree(nodes)
    s = Solution()
    s.levelOrder(tree.root)