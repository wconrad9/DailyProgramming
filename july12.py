#given an N x M matrix, print it out in a spiral

test = [[1,2, 3, 4, 5, 6],
        [6, 7, 8, 9, 10, 7],
        [11, 12, 13, 14, 15, 8],
        [16, 17, 18, 19, 20, 9],
        [1,2,3,4,5, 10]]

def print2(matrix):

    lowi = 0
    highi = len(matrix) - 1
    lowj = 0
    highj = len(matrix[0]) - 1

    printed = 0
    while printed < len(matrix) * len(matrix[0]):

        i = lowi
        j = lowj

        if printed + 1 == len(matrix) * len(matrix[0]):
            print(matrix[i][j])
            printed += 1

        while j < highj and printed < len(matrix) * len(matrix[0]):
            print(matrix[i][j])
            printed += 1
            j+=1
        highj -=1
        while i < highi and printed < len(matrix) * len(matrix[0]):
            print(matrix[i][j])
            printed += 1
            i +=1
        highi -= 1
        while j > lowj and printed < len(matrix) * len(matrix[0]):
            print(matrix[i][j])
            printed += 1
            j -= 1
        lowj += 1
        while i > lowi and printed < len(matrix) * len(matrix[0]):
            print(matrix[i][j])
            printed += 1
            i -=1
        lowi += 1
        #print(i,j, printed)

    



def printClockwiseSpiral(matrix) -> None:
    """print out the contents of an N x M matrix in a clockwise spiral"""

    #print first row

    lowi = 0
    highi = len(matrix)
    lowj = 0
    highj = len(matrix[0])

    printed = 0

    i = 0
    j = 0
    while printed < len(matrix) * len(matrix[0]):
        i, j = lowi, lowj
        while j < highj - 1:
            print(matrix[i][j])
            printed += 1
            j+=1
        highj -= 1
        while i < highi - 1:
            print(matrix[i][j])
            printed += 1
            i += 1
        highi -= 1
        while j >= lowj + 1:
            print(matrix[i][j])
            printed += 1
            j -= 1
        lowj += 1
        while i >= lowi + 1:
            print(matrix[i][j])
            printed += 1
            i -= 1
        lowi += 1

    return

print2(test)