# Find Successor

"""
Write am fucntion that takes in a Binary Tree (where nodes have an additional pointer to their parent node) as well as a node contained in that tree and returns the given node's successor.

A node's successor is the next node to be visited (immediately after the given node) when traversing its tree using the in-order tree-traversal technique. A node has no successor if it's the last node to be visited in the in-order traversal.

If a node has no successor, your function should return None / null.

Each BinaryTree node has an integer value, a parent node, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =             1    <-- root    
                 /   \
                2     3
               / \  
              4   5
             /
            6

node = 5

Sample Output
1
// Thus tree's in-order traversal order is: 6 -> 4 -> 2 -> 5 -> 1 -> 3
// 1 comes immediately after 5.


"""

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# Brute Force Approach: In-Order Traversal

def inOrderTraversal(tree, array):
    if tree is None:
        return
    inOrderTraversal(tree.left, array)
    array.append(tree)
    inOrderTraversal(tree.right, array)

# Time: O(n) | Space: O(n)
def findSuccessor(tree, node):
    inOrderTraversalArray = []
    inOrderTraversal(tree, inOrderTraversalArray)
    for i in range(len(inOrderTraversalArray)):
        if node.value == inOrderTraversalArray[i].value and i != len(inOrderTraversalArray) - 1:
            return inOrderTraversalArray[i+1]
    return None


# Optimal Approach: Iterative In-Order Traversal

def getLeftmostChild(node):
    currentNode = node
    while currentNode.left is not None:
        currentNode = currentNode.left
    return currentNode

def getRightmostParent(node):
    currentNode = node
    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent
    return currentNode.parent


# Time: O(h) | Space: O(1)
def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftmostChild(node.right)
    return getRightmostParent(node)
