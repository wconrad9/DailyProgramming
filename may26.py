array = [10, 5, 2, 7, 8, 7]

k = 3

def maxSubArrays(array, k):


    for i in range(0, len(array) - (k-1)):
        counter = 0
        max = 0
        while counter < k:
            if array[counter + i] > max:
                max = array[counter + i]
            counter+=1
        print(max)


maxSubArrays(array, k)
