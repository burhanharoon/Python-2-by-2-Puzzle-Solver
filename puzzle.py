initialState = [0, 3, 2, 1]
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


def performOpoerations(node, opr1, opr2, queue):
    temp1 = opr1(node)
    temp2 = opr2(node)
    if temp1 not in visited:
        queue.append(temp1)
    if temp2 not in visited:
        queue.append(temp2)


def puzzle(queue, initialState, visited, goalState):
    queue.append(initialState)
    global found
    found = False
    while(queue):
        node = queue.pop(0)
        last = node
        visited.append(node)
        if compareNodes(node, goalState):
            print("Goal node found")
            found = True
            break
        else:
            indexOfZero = node.index(0)
            if indexOfZero == 0:
                performOpoerations(node, moveDown, moveRight, queue)
            elif indexOfZero == 1:
                performOpoerations(node, moveDown, moveLeft, queue)
            elif indexOfZero == 2:
                performOpoerations(node, moveUp, moveRight, queue)
            elif indexOfZero == 3:
                performOpoerations(node, moveUp, moveLeft, queue)


puzzle(queue, initialState, visited, goalState)

print("The visited path is: ", visited) if found else print(
    "The goal state cannot be found")
