testBoard = [[False,False,False,False],
[True,True,False,True],
[False,False,False,False],
[False,False,False,False]]

#characteristics of valid move:
#1) not True square
#2) i,j within board
#   a) i < len(board)
#   b) i >= 0
#   c) j < len(board[0])
#   d) j >= 0
#3) square not yet visited
def isValid(i,j, board, visited):
    return not(i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or board[i][j] == True or visited[i][j] == 1)

def shortestBoardPath(board, start, end):
    """return the shortest valid path through the board using Lee's BFS"""

    class node:
        
        def __init__(self, coord, dist):
            self.coord = coord
            self.dist = dist

    #initialize 2D array to store the locations visited
    visited = [[0] * len(board[0]) for num in range(len(board))]

    if isValid(start[0], start[1], board, visited):
        visited[start[0]][start[1]] = 1

    #initialize start node
    startNode = node((start[0], start[1]), 0)

    #initialize queue to hold nodes in BFS
    q = []
    #append root of BFS
    q.append(startNode)

    #start while loop BFS

    while len(q) > 0:

        #pop the first node and use as root for search
        currentNode = q.pop(0)

        #check if the node is the destination/end
        if currentNode.coord == end:
            return currentNode.dist

        #otherwise, BFS

        #left
        if isValid(currentNode.coord[0], currentNode.coord[1]-1, board, visited):
            visited[currentNode.coord[0]][currentNode.coord[1]-1] = 1
            q.append(node((currentNode.coord[0], currentNode.coord[1]-1), currentNode.dist + 1))

        #right
        if isValid(currentNode.coord[0], currentNode.coord[1]+1, board, visited):
            visited[currentNode.coord[0]][currentNode.coord[1]+1] = 1
            q.append(node((currentNode.coord[0], currentNode.coord[1]+1), currentNode.dist + 1))

        #up
        if isValid(currentNode.coord[0]-1, currentNode.coord[1], board, visited):
            visited[currentNode.coord[0]-1][currentNode.coord[1]] = 1
            q.append(node((currentNode.coord[0]-1, currentNode.coord[1]), currentNode.dist + 1))
        
        #down
        if isValid(currentNode.coord[0] +1, currentNode.coord[1], board, visited):
            visited[currentNode.coord[0] + 1][currentNode.coord[1]] = 1
            q.append(node((currentNode.coord[0]+1, currentNode.coord[1]), currentNode.dist + 1))
        
        print(visited)

        #if no path is found
    return -1

print(shortestBoardPath(testBoard, (3,0),(0,0)))