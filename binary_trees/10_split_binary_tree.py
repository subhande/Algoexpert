"""
Write a function that takes in a Binary Tree with at least one node and checks if that Binary Tree can be split into two Binary Trees of equal sum by removing a single edge. If this split is possible, return the new sum of each Binary Tree, otherwise return 0. Note that you do not need to return the edge that was removed.

The sum of a Binary Tree is the sum of all values in that Binary Tree.

Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.


Sample Input
tree =     1
         /   \
       3     -2
     /  \   /  \
    6   -5 5    2
  /
 2 

Sample Output
   // Remove the edge to the left of the root node.
 6 // creating two trees, each with sums of 6


"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def getTreeSum(tree):
    if tree is None:
        return 0
    return tree.value + getTreeSum(tree.left) + getTreeSum(tree.right)

# Time: O(n) | Space: O(h)
def splitBinaryTree(tree):
    disiredSubtreeSum = getTreeSum(tree) / 2
    canBeSplit = trySubtrees(tree, disiredSubtreeSum)[1]
    return disiredSubtreeSum if canBeSplit else 0

# Time: O(n) | Space: O(h)
def trySubtrees(tree, disiredSubtreeSum):
    if tree is None:
        return (0, False)

    leftSubtreeSum, leftCanSplit = trySubtrees(tree.left, disiredSubtreeSum)
    rightSubtreeSum, rightCanSplit = trySubtrees(tree.right, disiredSubtreeSum)

    currentSum = tree.value + leftSubtreeSum + rightSubtreeSum
    canSplit = leftCanSplit or rightCanSplit or currentSum == disiredSubtreeSum
    return (currentSum, canSplit)