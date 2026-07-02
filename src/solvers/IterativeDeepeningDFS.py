def limitedDFS(node, goal, limit, currentPath):
    path = currentPath + [node]

    if node.state == goal:
        return path

    if limit <= 0:
        return None

    for action in node.getActions():
        neighbor = node.applyAction(action)

        if neighbor in path:
            continue
    
        resultingPath = limitedDFS(neighbor, goal, limit - 1, path)

        if resultingPath is not None:
            return resultingPath


def iterativeDeepeningDFS(start, goal, maxDepth):
    for limit in range(maxDepth + 1):
        path = limitedDFS(start, goal, limit, [])

        if path is not None:
            return path
    
    return None

'''
Notes to self:
I need a way to keep track of the cube states in a graph which also keeps info like:
- what action was taken to get to state
- how many steps to get to path

The above could will need updating, a list won't be needed
To get path, just reverse actions from graph based on extra info listed above
'''