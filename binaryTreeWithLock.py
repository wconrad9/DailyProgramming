

class BinaryTreeWithLock():

    root = None

    class TreeNode():

        def __init__(self, val, parent = None, leftChild = None, rightChild = None):
            self.val = val
            self.parent = parent
            self.leftChild = leftChild
            self.rightChild = rightChild
            self.lockedDescendants = 0
            self.locked = False
    
    def isLocked(node: TreeNode):
        return node.locked

    def lock(self, node: TreeNode) -> bool:

        if node.locked:
            return True
        
        if not self.canUnlockOrLock(node):
            return False
        
        node.locked = True

        parentNode = node.parent
        while parentNode != None:
            parentNode.lockedDescendants += 1
            parentNode = parentNode.parent
        
        return True
    
    def unlock(self, node: TreeNode) -> bool:

        if not self.canUnlockOrLock(node):
            return False

        node.locked = False

        parentNode = node.parent
        while parentNode != None:
            parentNode.lockedDescendants -= 1
            parentNode = parentNode.parent

        return True

        
    def canUnlockOrLock(node):
        
        if node.lockedDescendants > 0:
            return False
        
        currentNode = node.parent

        while currentNode != None:
            if currentNode.isLocked():
                return False
            currentNode = currentNode.parent
        
        return True
    
    def insert(self, value):
        newNode = self.TreeNode(value)

        currentNode = self.root

        while(1):

            if currentNode.leftChild == None:
                currentNode.leftChild = newNode
                newNode.parent = currentNode
                return
            
            if currentNode.rightChild == None:
                currentNode.rightChild = newNode
                newNode.parent = currentNode
                return
            
            currentNode = currentNode.leftChild

    
    def printTree(self, node: TreeNode):

        if node.leftChild:
            self.printTree(node.leftChild)
        print(node.val)
        if node.rightChild:
            self.printTree(node.rightChild)

        return
        
        


l = BinaryTreeWithLock()

r = l.TreeNode(2)

l.root = r


leftChild = l.insert(1)
rightChild = l.insert(3)
leftChild2 = l.insert(5)
rightChild2 = l.insert(7)

l.lock(r)

l.printTree(l.root)


    
    