initialState = [1, 2, 0, 3]
goalState = [1, 2, 3, 0]

queue = [initialState]  # Starting node for the graph
visited = []  # Starting node for the graph


def compareNodes(node1, node2):
    if node1 == node2:
        return True
    else:
        return False


def checkVisitedNodes(visited, toCheckNode):
    flag = False
    for visitedNode in visited:
        if compareNodes(visitedNode, toCheckNode):
            flag = True

    if flag:
        return True
    else:
        return False


def moveUp(node):
    nodeCopy = []
    for x in node:
        nodeCopy.append(x)
    if node.index(0) == 2:
        temp = nodeCopy[0]
        nodeCopy[0] = 0
        nodeCopy[2] = temp
        return nodeCopy
    elif node.index(0) == 3:
        temp = nodeCopy[1]
        nodeCopy[1] = 0
        nodeCopy[3] = temp
        return nodeCopy


def moveDown(node):
    nodeCopy = []
    for x in node:
        nodeCopy.append(x)
    if node.index(0) == 0:
        temp = nodeCopy[2]
        nodeCopy[2] = 0
        nodeCopy[0] = temp
        return nodeCopy
    elif node.index(0) == 1:
        temp = nodeCopy[3]
        nodeCopy[3] = 0
        nodeCopy[1] = temp
        return nodeCopy


def moveRight(node):
    nodeCopy = []
    for x in node:
        nodeCopy.append(x)
    if node.index(0) == 0:
        temp = nodeCopy[1]
        nodeCopy[1] = 0
        nodeCopy[0] = temp
        return nodeCopy
    elif node.index(0) == 2:
        temp = nodeCopy[3]
        nodeCopy[3] = 0
        nodeCopy[2] = temp
        return nodeCopy


def moveLeft(node):
    nodeCopy = []
    for x in node:
        nodeCopy.append(x)
    if node.index(0) == 1:
        temp = nodeCopy[0]
        nodeCopy[0] = 0
        nodeCopy[1] = temp
        return nodeCopy
    elif node.index(0) == 3:
        temp = nodeCopy[2]
        nodeCopy[2] = 0
        nodeCopy[3] = temp
        return nodeCopy


while(len(queue) != 0):
    elem = (queue.pop(0))
    visited.append(elem)
    if compareNodes(elem, goalState):
        print("Goal node found")
        break
    else:
        indexOfZero = elem.index(0)
        if indexOfZero == 0:
            queue.append(moveDown(elem))
            queue.append(moveRight(elem))
        elif indexOfZero == 1:
            queue.append(moveLeft(elem))
            queue.append(moveDown(elem))
        elif indexOfZero == 2:
            queue.append(moveUp(elem))
            queue.append(moveRight(elem))
        elif indexOfZero == 3:
            queue.append(moveLeft(elem))
            queue.append(moveUp(elem))


print("The visited Path is:", visited)
