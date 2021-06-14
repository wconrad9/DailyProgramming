import itertools
from typing import List
from itertools import combinations


set = [1,2,3]

def powerSet(set) -> List:
    """return the superset of an input set"""

    output = []

    for i in range(len(set)+1):
        combs = combinations(set, i)

        for el in combs:
            print(el)
            output.append(list(el))


    return output
            

print(powerSet(set))
