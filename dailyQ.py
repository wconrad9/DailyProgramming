
import time
sample_list = [3,4,-1,1,-1, 2, 7, 6, 5]
sample_list2 = [1,2,0]

k = 17

def lowestPos(list, number):
    
    list = sorted(list)

    try: 
        list.index(number)
        return lowestPos(list, number+1)
    except:
        return number

print(lowestPos(sample_list, 1))

def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            print("palindrome num: ", num)
            print("i: ",  i)
            if i is not None:
                num = i
        num += 1

def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False

"""
pal_gen = infinite_palindromes()
for i in pal_gen:
    print("pal_gen contents: ", i)
    digits = len(str(i))
    if digits >= 5:
        pal_gen.throw(ValueError("can't handle such large numbers"))
    sendback = 10 ** (digits)
    print("sendback: ", sendback)
    pal_gen.send(sendback)
"""

#good start May 9

def listAddition(list, k):
    """do any two of the numbers from the list add up to k"""

    for idx in range(len(list) - 1):
        add1 = list[idx]
        for num in list[idx+1:]:
            if add1 + num == k:
                return True
    
    return False

def genAddition(list, k):
    """use a generator to solve the same problem"""

    #Todo: learn about python generators

    print()



def productExceptI(list):
    """given an array of integers, return an array where each index i instead represents the product
    of all the other numbers in the array except the number at i"""

    #multiply by every other number, then divide by number at i
    prodList = []
    for i, num in enumerate(list):
        
        accumulator = 1
        for idx in range(len(list)):
            accumulator *= list[idx]

        prodList.append(accumulator / num)

    return prodList

assert productExceptI([3,2,1]) == [2, 3, 6]


def prodWithoutDivision(list):

    prodList = []
    for i, num in enumerate(list[:len(list)]):

        accumulator = 1
        #multiply by all the numbers in the list except for i


        for num2 in list[:i] + list[i+1:]:
            accumulator *= num2
        
        prodList.append(accumulator)
    
    return prodList

assert prodWithoutDivision([1,2,3]) == [6, 3, 2]