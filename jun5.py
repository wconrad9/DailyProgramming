

from typing import Counter


def runLengthEncode(s):

    #save first character

    outstring = ""
    count = 1
    for index in range(len(s)-1):
        
        if s[index] == s[index+1]:
            count+=1

        else:
            outstring += str(count) + s[index]
            count = 1

    outstring += str(count) + s[index]

    print(outstring)


def runLengthDecode(s):

    #read s in two character chunks
    outstring = ""
    i = 0
    while i <= len(s) - 2:
        count = s[i]
        char = s[i+1]

        outstring += int(count) * char
        i+=2

    print(outstring)
    
            
runLengthEncode("AAAABBBCCDAA")
runLengthDecode("4A3B2C1D2A")