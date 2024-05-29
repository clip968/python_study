import queue
class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrder(self, node):
        if node is not None:
            print('[%c] ' % node.data, end='')
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        if node != None:
            self.inOrder(node.left)
            print('[%c] ' % node.data, end='')
            self.inOrder(node.right)

    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print('[%c] ' % node.data, end='')

    def levelOrder(self, node):
        Q = queue.Queue()
        Q.put(node)

        while not Q.empty():
            node = Q.get()
            print('[%c] ' %node.data, end='')

            if node.left != None:
                Q.put(node.left)
            
            if node.right != None:
                Q.put(node.right)

    def nodeCount(self, node):
        count = 0
        if node != None:
            count = 1 + self.nodeCount(node.left) \
                + self.nodeCount(node.right)
            
        return count
    
    def isExternal(self, node):
        return node.left == None and node.right == None
    
    def leafCount(self, node):
        count = 0
        if node != None:
            if self.isExternal(node):
                return 1
            else:
                count = self.leafCount(node.left) \
                    + self.leafCount(node.right)
            
        return count
    
    def getHeight(self, node):
        if node == None:
            return 0
        return max(self.getHeight(node.left), self.getHeight(node.right) + 1)

if __name__ == "__main__":
    T = BinaryTree()
    
    n6 = TreeNode('F')
    n5 = TreeNode('E')
    n4 = TreeNode('D', )
    n3 = TreeNode('C', n6)
    n2 = TreeNode('B', n4, n5)
    n1 = TreeNode('A', n2, n3)

    print('Pre : ', end=''); T.preOrder(n1); print()
    print('In : ', end=''); T.inOrder(n1); print()
    print('Post : ', end=''); T.postOrder(n1); print()
    print('Level : ', end=''); T.levelOrder(n1); print()

    print("Node Count : %d" %T.nodeCount(n1))
    print("Leaf Count : %d" %T.leafCount(n1))
    
