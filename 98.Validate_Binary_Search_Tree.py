def isValidBST(root):
    def bfs(node, lower=float("-inf"), upper=float("inf")):
        if not node:
            return True
        if node.val <= lower or node.val >= upper:
            return False
        if not bfs(node.right, node.val, upper):
            return False
        if not bfs(node.left, lower, node.val):
            return False
        return True

    return bfs(root)
