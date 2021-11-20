initialState = [3, 2, 1, 0]
goalState = [1, 2, 3, 0]

queue = []
visited = []


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


def puzzle(queue, initialState, visited, goalState):
    queue.append(initialState)

    while(queue):
        elem = queue.pop(0)
        visited.append(elem)
        if compareNodes(elem, goalState):
            print("Goal node found")
            break
        else:
            indexOfZero = elem.index(0)
            if indexOfZero == 0:
                temp1 = moveDown(elem)
                temp2 = moveRight(elem)
                if temp1 not in visited:
                    queue.append(temp1)
                if temp2 not in visited:
                    queue.append(temp2)
            elif indexOfZero == 1:
                temp1 = moveLeft(elem)
                temp2 = moveDown(elem)
                if temp1 not in visited:
                    queue.append(temp1)
                if temp2 not in visited:
                    queue.append(temp2)
            elif indexOfZero == 2:

                temp1 = moveUp(elem)
                temp2 = moveRight(elem)
                if temp1 not in visited:
                    queue.append(temp1)
                if temp2 not in visited:
                    queue.append(temp2)
            elif indexOfZero == 3:
                temp1 = moveLeft(elem)
                temp2 = moveUp(elem)
                if temp1 not in visited:
                    queue.append(temp1)
                if temp2 not in visited:
                    queue.append(temp2)


puzzle(queue, initialState, visited, goalState)
print("The visited Path is:", visited)
