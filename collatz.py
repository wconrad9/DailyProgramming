

def sequence(startingNumber):

    currentNumber = startingNumber
    moves = 1

    while(currentNumber != 1):

        if currentNumber % 2 == 0:
            currentNumber /= 2
            moves+=1
        else:
            currentNumber = (currentNumber * 3) + 1
            moves+=1

    return [startingNumber, moves]

"""
for integer in range(1, 1000000):
    maxMoves = 0
    maxStart = 0
    
    if sequence(integer)[1] > maxMoves:
        maxMoves = sequence(integer)[1]
        maxStart = sequence(integer)[0]
    
    print(integer/1000000 * 100)
    
print(maxMoves, maxStart)

"""
print(sequence(999999))