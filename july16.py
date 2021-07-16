from itertools import combinations

test = [-10,-20,2,5]

def max3product(array) -> int:
    """returns the maximum product from 3 members of an array - brute force"""

    prods = []
    for comb in combinations(test, 3):
        prods.append(comb[0]*comb[1]*comb[2])

    return max(prods)

class max3product:

    def max3Product(self):
        prods = []
        for comb in combinations(self.array, 3):
            prods.append(comb[0]*comb[1]*comb[2])

        return max(prods)

    def __init__(self, array) -> None:
        self.array = array
        self.prod = self.max3Product()

    class printer:

        def __init__(self, array) -> None:
            self.array = array
        
        def toString(self):

            for s in self.array:
                print(s)


class max4product(max3product):

    def __init__(self, array) -> None:
        super().__init__(array)
        self.max4Product = self.max4Product()

    def max4Product(self):
        prods = []
        for comb in combinations(self.array, 4):
            prods.append(comb[0]*comb[1]*comb[2]*comb[3])
    
        return max(prods)

    class printer(max3product.printer):

        def __init__(self, array) -> None:
            super().__init__(array)


        def toString(self):

            for s in self.array:
                print("val ", s)


def dec2bin(dec)->int:
    pass
    

def binaryCounter(length):

    combs = []
    max = pow(2, length)
    print(max)
    i = 1
    while i <= max:
        print(bin(i)[2:])
        i+=1
    
    return

print(binaryCounter(4))

print(xrange(4))