def area(Z):

    #return max area of input in Z making a rectangle with straws

    length = int(Z) // 2
    
    areas = []

    while length >= 1:

        width = (int(Z) - length * 2) // 2

        if width <= 1:
            length -= 1
            continue

        if not length == width:
            areas.append(length * width)
        
        print(length)
        length -= 1
    
    return max(areas)

print(area(input()))