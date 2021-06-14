from typing import Mapping


alphabet = 'abcdefghijklmnopqrstuvwxyz'

map = {str(ord(letter) - 96):letter for letter in alphabet}

print(map)

def countDecodings(encoded):
    """how many ways can encoded be decoding using mapping"""

    #need to split message into all combinations of bigrams and unigrams

    if len(encoded) == 1:
        return 1
    elif len(encoded) == 2:
        try:
            map[encoded]
            if encoded[1] == '0' or encoded[1] == ['1']:
                return 1
            else:
                return 2
        except:
            return 1
    elif len(encoded) == 0:
        print(encoded)
        return 0
    else:
        try:
            map[encoded[0:2]]
            print(encoded)
            return countDecodings(encoded[2:]) + countDecodings(encoded[1:])
        except:
            print(encoded)
            return countDecodings(encoded[1:])



print(countDecodings('18122312'))

