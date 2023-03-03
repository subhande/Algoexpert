# Find the kth largest value in a BST

"""
Write a function that takes in a Binary Search Tree (BST) and a positive integer k and returns the kth largest integer contained in the BST.

You can assume that there will only be integer values in the BST and that k is less than or equal to the number of nodes in the tree.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.

Sample Input
tree =            10
                /    \
                5      15
                / \    /  \
                2   5  13  22
                /        \
                1          14
k = 3

Sample Output
15

"""

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Solution 1: Brute Force Approach
# Time: O(n) | Space: O(n)
def findKthLargestValueInBst(tree, k):
    sortedNodeValues = []
    inOrderTraversal(tree, sortedNodeValues)
    return sortedNodeValues[-k]


def inOrderTraversal(tree, sortedNodeValues):
    if tree is None:
        return
    inOrderTraversal(tree.left, sortedNodeValues)
    sortedNodeValues.append(tree.value)
    inOrderTraversal(tree.right, sortedNodeValues)


# Solution 2: Optimized Approach

class TreeInfo:
    def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
        self.numberOfNodesVisited = numberOfNodesVisited
        self.latestVisitedNodeValue = latestVisitedNodeValue

# Time: O(h + k) => O(h) | Space: O(h)
def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraversal (tree, k, treeInfo)
    return treeInfo.latestVisitedNodeValue

def reverseInOrderTraversal(node, k, treeInfo):
    if node == None or treeInfo.numberOfNodesVisited >= k:
        return
    reverseInOrderTraversal(node.right, k, treeInfo)
    if treeInfo.numberOfNodesVisited < k:
        treeInfo.numberOfNodesVisited += 1
        treeInfo.latestVisitedNodeValue = node.value
        reverseInOrderTraversal(node.left, k, treeInfo)
    
    