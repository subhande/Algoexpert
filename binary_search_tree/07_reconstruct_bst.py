# Reconstruct BST

"""
The pre-order traversal of a BST is a traversal technique that starts at the tree's root node and visits nodes in the following order: 

1. Current node
2. Left subtree
3. Right subtree. 

Given non-empty array of integers representing the pre-order traversal of a Binary Search Tree (BST), Write a function that creates the relevant BST and returns its root node. 

The input array will contain the values of BST nodes in the order in which these nodes would be visited with a pre-order traversal.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.

A BST is valid if and only if all of its nodes are valid BST nodes.

Sample Input

preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]

Sample Output

This is what the BST looks like:

        10
      /    \
     4      17
    / \       \
   2   5      19
  /          /
 1          18


"""

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
# _________________________________________________________________
# Brute Force Approach 1
# _________________________________________________________________
# Avg: Time: O(nlogn) | Space: O(h)
# Worst: Time: O(n^2) | Space: O(h)
def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return None
    bst = BST(preOrderTraversalValues[0])
    for ele in preOrderTraversalValues[1:]:
        bst.insert(ele)
    return bst

# _________________________________________________________________
# Brute Force Approach 2
# _________________________________________________________________
# Time: O(n^2) | Space: O(n)
"""
preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]

[10 , 4, 2, 1, 5, 17, 19, 18]
 ---  ----------  ----------
 root  left tree  right tree

[4,    2, 1,     5]
 ____  ____      ----
 root  left     right
"""
def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return None
    currentValue = preOrderTraversalValues[0]
    rightSubtreeRootIdx = len(preOrderTraversalValues)
    for idx in range(1, len(preOrderTraversalValues)):
        value = preOrderTraversalValues[idx]
        if value >= currentValue:
            rightSubtreeRootIdx = idx
            break
    leftSubtree = reconstructBst(preOrderTraversalValues[1:rightSubtreeRootIdx])
    rightSubtree = reconstructBst(preOrderTraversalValues[rightSubtreeRootIdx:])
    bst = BST(currentValue, leftSubtree, rightSubtree)
    return bst


# _________________________________________________________________
# Optimal Approach 1
# _________________________________________________________________
# Time: O(n^2) | Space: O(h)
"""
preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]

[10 , 4, 2, 1, 5, 17, 19, 18]
 ---  ----------  ----------
 root  left tree  right tree

[4,    2, 1,     5]
 ____  ____      ----
 root  left     right
"""


class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx

def reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo):
    if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
        return None
    rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]
    if rootValue < lowerBound or rootValue >= upperBound:
        return None
    currentSubtreeInfo.rootIdx += 1
    leftSubtree = reconstructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo)
    rightSubtree = reconstructBstFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubtreeInfo)
    bst = BST(rootValue, leftSubtree, rightSubtree)
    return bst

# Time: O(n) | Space: O(h)
def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(float("-inf"), float("inf"), preOrderTraversalValues, treeInfo)