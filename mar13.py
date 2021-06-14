class xorLinkedList:

    def __init__(self) -> None:
        pass
        

class Node:

        def __init__(self) -> None:
            self.next = None
            self.prev = None
            self.idx = None

        def hasNext(self):

            if self.next == None:
                return False
            else:
                return True

class doublyLinkedList:

    startNode = None
    currentNode = None

    #initialized with index zero
    def __init__(self) -> None:
        self.startNode = Node()
        self.startNode.idx = 0
        self.currentNode = self.startNode
    
    #add a node to the list
    def addNode(self):
        nextNode = Node()
        nextNode.prev = self.currentNode
        self.currentNode.next = nextNode
        self.currentNode = nextNode
        nextNode.idx = nextNode.prev.idx + 1

    def removeNode(self, idx):
        node = self.startNode

        while node.idx != idx:

            node = node.next
        
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        while node.hasNext():
            node.next.idx -= 1
            node = node.next

    def printNodes(self):

        self.currentNode = self.startNode
        print(self.currentNode.idx)
        while self.currentNode.hasNext():
            print("idx: ", self.currentNode.next.idx)
            self.currentNode = self.currentNode.next


dll = doublyLinkedList()

dll.addNode()
dll.addNode()
dll.addNode()
dll.removeNode(0)

dll.printNodes()
