def canFinish(numCourses, prerequisites):
    if numCourses > len(prerequisites) or len(prerequisites) == 0:
        return True
    

    pre = {}
    for item in prerequisites:
        pre[item[0]] = item[1]
        
    stack = []
    visited = []
    for item in prerequisites:
        visited.append(item[0])
        stack.append(item[1])
    while stack:
        course = stack.pop()
