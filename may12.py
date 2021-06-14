

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    """return the first element of a pair"""
    
    def createArray(a,b):
        array = []
        array.append(a)
        array.append(b)
        return array
    
    #perform closure
    array = pair(createArray)

    return array[0]

def cdr(pair):
    """return the first element of a pair"""
    
    def createArray(a,b):
        array = []
        array.append(a)
        array.append(b)
        return array
    
    #perform closure
    array = pair(createArray)

    return array[1]


print(car(cons(3,4)))
print(cdr(cons(3,4)))
