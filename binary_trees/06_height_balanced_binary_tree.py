# Height Balanced Binary Tree

"""
You're given the root node of a Binary Tree. Write a function that returns true if this Binary Tree is height balanced and false if it isn't.

A Binary Tree is height balanced if for each node in the tree, the difference between the height of its left subtree and the height of its right subtree is at most 1.

Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =             1    <-- root
                 /   \
                2     3
               / \   / \
              4   5 6   7
             / \
            8   9


Sample Output
false
"""

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, isBalanced):
        self.isBalanced = isBalanced

def heightBalancedBinaryTreeHelper(tree, height, treeInfo):
    if tree is None:
        return height

    leftHeight = heightBalancedBinaryTreeHelper(tree.left, height + 1, treeInfo)
    rightHeight = heightBalancedBinaryTreeHelper(tree.right, height + 1, treeInfo)

    if abs(leftHeight - rightHeight) > 1:
        treeInfo.isBalanced = False

    return max(leftHeight, rightHeight)

def heightBalancedBinaryTree(tree):
    treeInfo = TreeInfo(True)
    heightBalancedBinaryTreeHelper(tree, 0, treeInfo)
    return treeInfo.isBalanced

