
from typing import Sequence


def pathCount(stairs: int):
    """number of unique ways to climb N stairs using 1 or 2 steps"""

    #we've reached the top
    if stairs == 0:
        return 1
    else:
        if stairs < 2:
            return pathCount(stairs - 1)
        return pathCount(stairs - 2) + pathCount(stairs - 1)

def pathCountX(stairs: int, X):
    """number of unique ways to climb N stairs using 1 or 2 steps"""

    #we've reached the top
    if stairs == 0:
        return 1
    elif stairs < 0:
        return 0
    else:
        validSteps = []
        for num in X:
            if stairs >= num:
                validSteps.append(num)

        sum = 0
        for steps in validSteps:
            sum += pathCountX(stairs - steps, X)
        
        return sum
        

print(pathCountX(7, [1,3,5,7]))

