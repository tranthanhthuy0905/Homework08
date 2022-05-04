class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.children = []
        self.parent = None
        self.size = 1
        
    def addChild(self, child):
        child.parent = self
        self.children.append(child)
        self.size += 1

    def getSize(self, treeNode, size):
        if len(treeNode.children) == 0:
            return size
        
        size += len(treeNode.children)
        for child in treeNode.children:
            if child.children != []:
                size += len(child.children)
                return self.getSize(child.children, size)
        return size
                
    def creatingTree(self):
        node0 = TreeNode(0)
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node0.addChild(node2)

        node3 = TreeNode(3)
        node0.addChild(node3)

        node4 = TreeNode(4)
        node2.addChild(node4)

        node5 = TreeNode(5)

        node6 = TreeNode(6)
        node6.addChild(node5)
        node6.addChild(node1)
        node2.addChild(node6)

        node7 = TreeNode(7)
        node8 = TreeNode(8)

        node9 = TreeNode(9)
        node2.addChild(node9)
        node9.addChild(node7)
        node9.addChild(node8)

        return node0
