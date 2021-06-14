from typing import Counter
count = 0
data = 0

class LinkedList:

    def __init__(self, head = None) -> None:
        self.head = head

    count = 0

    class node:

        def __init__(self, data, next = None) -> None:
            self.data = data
            self.next = next
    
        def hasnext(self):
            if self.next != None:
                return True
            else:
                return False
    
    def insert(self, data):
        curr = self.head

        while curr.hasnext():
            curr = curr.next
        
        curr.next = self.node(data)

    def printNodes(self):

        curr = self.head

        print(curr.data)

        while curr.hasnext():
            print(curr.next.data, id(curr))
            curr = curr.next
    
    def kthLastElement(self, k) -> int:

        head = self.head

        kcount = 1
        while kcount < k:
            head = head.next
            kcount+=1

        tail = self.head

        while head.hasnext():
            head = head.next
            tail = tail.next
        
        return tail.data


    def recursiveKthLastElement(self, node, k, depth = 0) -> int:

        global count
        global data

        if node.next == None:
            return 1

        self.recursiveKthLastElement(node.next, k, depth + 1)

        count = count + 1

        if count == k:
            print(node.data)
            data = node.data
        
        return data
        



    

ll = LinkedList()

ll.head = ll.node(1)

ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)

print(ll.recursiveKthLastElement(ll.head, 2))






        
            