"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
import collections

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        queue = collections.deque([node])
        visited = {node: Node(node.val,[])}
        while queue:
            n = queue.popleft()
            for item in n.neighbors:
                if item not in visited:
                    visited[item] = Node(item.val,[])
                    queue.append(item)
                visited[n].neighbors.append(visited[item])
        return visited[node]


