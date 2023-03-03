# Binary Tree Diameter

"""
Write a function that takes in a Binary Tree and returns its diameter. The diameter of a binary tree is defined as the length of its longest path, even if that path doesn't pass through the root of the tree.

A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes; a path sum is the sum of the values of the nodes in a particular path.

Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =             1    <-- root
                 /   \
                3     2
               / \
              7   4
             /     \
            8       5
           /         \
          9           6

Sample Output
6 // 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6
// There are 6 edeges between the first and the last node of this tree's longest path.




"""

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Approach 1

class TreeInfo:
    def __init__(self, diameter):
        self.diameter = diameter

# Time: O(n) | Space: O(h)
def binaryTreeDiameter(tree):
    treeInfo = TreeInfo(0)
    binaryTreeDiameterHelper(tree, 0, treeInfo)
    return treeInfo.diameter

def binaryTreeDiameterHelper(tree, height, treeInfo):
    if tree is None:
        return 0
    leftHeight = binaryTreeDiameterHelper(tree.left, height, treeInfo)
    rightHeight = binaryTreeDiameterHelper(tree.right, height, treeInfo)
    height = max(leftHeight, rightHeight) + 1
    treeInfo.diameter = max(leftHeight + rightHeight, treeInfo.diameter)
    return height



# Approach 1

class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height

# Time: O(n) | Space: O(h)
def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    diameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currentDiameter = max(longestPathThroughRoot, diameterSoFar)
    currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)
    return TreeInfo(currentDiameter, currentHeight)