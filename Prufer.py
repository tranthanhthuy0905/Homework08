from TreeNode import TreeNode

def checkSmallestLeaf(treeNode, listCheck):
    
    # Base statement
    if treeNode.parent is None and treeNode.children == []:
        listCheck.append(treeNode.val)
        return min(listCheck)
    
    # Recursive statements
    # Get children
    children = treeNode.children
    for child in children:
        if child.children == []:
            return listCheck.append(child.val)
        else:
            return checkSmallestLeaf(child)
    return min(listCheck)
                
def encodingTree():
    pruferArr = []
    # Creating a tree with root - 0
    tree = TreeNode.creatingTree(0)
    print(tree.getSize(tree, 0))
    #for i in range(tree.size): 
encodingTree()
        
        
        
        
        