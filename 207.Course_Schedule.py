class Solution:
    def canFinish(self,numCourses,prerequisites):
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        for pair in prerequisites:
            x,y = pair
            graph[x].append(y)
            
        for i in range(numCourses):
            if not self.dfs(graph,visited,i):
                return False
        return True

    def dfs(self,graph,visited,i):

        # if the path has been visited and there is a cycle...
        if visited[i] == -1:
            return False
        
        # if the path has been visited and is valid
        if visited[i] == 1:
            return True

        visited[i] = -1
        for j in graph[i]:
            if not self.dfs(graph,visited,j):
                return False

        visited[i] = 1
        return True




