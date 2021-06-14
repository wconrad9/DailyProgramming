from typing import List


test = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "surelydid", "I", "saw", "it","was", "yesterday"]

    
class LinkedList:

    def __init__(self, head) -> None:
        self.head = self.node(head)

    class node:

        def __init__(self, word) -> None:
            self.word = word
            self.next = None
            self.length = len(word)

        def hasnext(self):

            if self.next != None:
                return True
            else:
                return False

    def insert(self, word):
        head = self.head

        while head.hasnext():
            head = head.next
        
        head.next = self.node(word)

    def printNodes(self):

        head = self.head

        while head.hasnext():
            print(head.word)
            head = head.next
        
        print(head.word)

"""
def justifyText(wordList, k) -> List[str]:

    words = LinkedList(wordList[0])

    output = []

    for word in wordList[1:]:
        words.insert(word)

    iterator = words.head
    acc = iterator.length

    sentence = ""
    while iterator.hasnext():

        if acc < k:
            sentence += iterator.word + " "
            acc += iterator.length + 1
            print("sentence: ", sentence, "acc", acc)
        
        else:
            output.append(sentence)
            sentence = ""
            sentence+=iterator.word + " "
            acc = iterator.length
            print(acc)
        
        print(iterator.word)

        iterator = iterator.next

    
    print(output)
"""

def justifyText(test,k):

    lineLength = 0
    lineWords = 0

    output = []

    sentence = []
    for word in test:
        lineLength += len(word)
        lineWords += 1
        print("word", word, "lineLength", lineLength)

        if lineLength + (lineWords - 1) <= k:
            sentence.append(word)
        else:
            output.append(sentence)
            sentence = []
            sentence.append(word)
            lineLength = len(word)
            lineWords = 1
    output.append(sentence)

    finalOutput = []

    for line in output:
        finalOutput.append(justify(line, k))

    print(finalOutput)
    

def justify(line, k):

    linelength = 0
    for word in line:
        linelength += len(word)

    spaces = k - linelength
    print(spaces)
    
    if len(line) == 1:
        while spaces > 0:
            line[0] += " "
            spaces -= 1
    else:
        index = 0
        while spaces > 0:
            print(line)
            line[index] += " "
            spaces -= 1
            index += 1
            if index == len(line) - 1:
                index = 0
    
    sentence = ""
    for word in line:
        sentence += word
    
    return sentence


    
    




justifyText(test, 16)
