# Max Path Sum in Binary Tree

"""
Write a function that takes in a Binary Tree and returns its max path sum. 

A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes; a path sum is the sum of the values of the nodes in a particular path.

Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree = 1
    / \
   2   3
  / \ / \
 4  5 6  7

Sample Output
18 // 5 + 2 + 1 + 3 + 7

"""

# Time:  O(n) | Space: O(log(n))
def maxPathSum(tree):
    _, maxPathSum = findMaxSum(tree)
    return maxPathSum


def findMaxSum(tree):
    if tree is None:
        return (0, float("-inf"))

    (
        leftMaxPathSumAsBranch,
        leftMaxPathSum,
    ) = findMaxSum(tree.left)
    rightMaxPathSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)

    maxChildSumAsBranch = (leftMaxPathSumAsBranch, rightMaxPathSumAsBranch)
    value = tree.value
    maxSumAsBranch = max(value, value + maxChildSumAsBranch)
    maxSumAsRootNode = max(leftMaxPathSumAsBranch + value + rightMaxPathSumAsBranch, maxSumAsBranch)

    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)

    return (maxSumAsBranch, maxPathSum)
