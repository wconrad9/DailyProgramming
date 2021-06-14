from collections import deque

testBoard = [[False,False,False,False],
[True,True,False,True],
[False,False,False,False],
[False,False,False,False]]

def isValid(i,j, visited, board):
    if i < 0:
        return False
    elif j < 0:
        return False
    elif i >= len(board):
        return False
    elif j >= len(board[0]):
        return False
    elif board[i][j] == True:
        return False
    elif visited[i][j]:
        return False
    else:
        return True

def solveBoard(board, start, end) -> int:
    """find the shortest path through the board"""

    class node:
        def __init__(self, value, dist):
            self.v = value
            self.dist = dist
    
    visited = [[0] * len(board[0]) for i in range(len(board))]

    q = []

    q.append(node(start, 0))

    visited[start[0]][start[1]] == 1

    while not (len(q) == 0):

        tempElement = q.pop(0)
        print(tempElement.v,  tempElement.dist)

        if tempElement.v[0] == end[0] and tempElement.v[1] == end[1]:
            print(tempElement.v[0], tempElement.v[1])
            return tempElement.dist

        #down
        if isValid(tempElement.v[0] + 1 ,tempElement.v[1], visited, board):
            q.append(node((tempElement.v[0]+1, tempElement.v[1]), tempElement.dist + 1))
        
        #up
        if isValid(tempElement.v[0] - 1 ,tempElement.v[1], visited, board):
            q.append(node((tempElement.v[0]-1, tempElement.v[1]), tempElement.dist +1))
        
        #right
        if isValid(tempElement.v[0],tempElement.v[1] + 1, visited, board):
            q.append(node((tempElement.v[0], tempElement.v[1]+1), tempElement.dist + 1))
        
        #left
        if isValid(tempElement.v[0],tempElement.v[1] - 1, visited, board):
            q.append(node((tempElement.v[0], tempElement.v[1]-1), tempElement.dist+1))
        
    return -1



print(solveBoard(testBoard, (3,0),(0,0)))





