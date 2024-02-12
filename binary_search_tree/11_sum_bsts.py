# Sum BSTs

"""
You're given a Binary Tree. As with any Binary Tree, this tree may contain one or more Binary Search Trees (BSTs), and it may even be a BST itself.

Write a function that returns the sum of all the values of nodes in this tree which are part of a BST containing at least 3 nodes.

Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

A BST is a special type of Binary Tree whose nodes all satisfy the BST property. A node satisfies the BST property if its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid Bst nodes themselves or
None / null.

# Sample Input 1

tree =     8
        /   \
       2     9
     /  \      \
    1    10     5

# Sample Output

13 // 1, 2 and 10 form the only BST containing atleast 3 nodes.

# Sample Input 2






"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, isBst, maxValue, minValue, bstSum, bstSize, totalSumBstNodes):
        self.isBst = isBst
        self.maxValue = maxValue
        self.minValue = minValue
        self.bstSum = bstSum
        self.bstSize = bstSize
        self.totalSumBstNodes = totalSumBstNodes


# Time: O(n) | Space: O(h)
def sumBsts(tree):
    return getTreeInfo(tree).totalSumBstNodes


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(True, float("-inf"), float("inf"), 0, 0, 0)
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    satisfiedBstProp = tree.value > leftTreeInfo.maxValue and tree.value <= rightTreeInfo.minValue

    isBst = satisfiedBstProp and leftTreeInfo.isBst and rightTreeInfo.isBst

    maxValue = max(tree.value, max(leftTreeInfo.maxValue, rightTreeInfo.maxValue))
    minValue = min(tree.value, max(leftTreeInfo.minValue, rightTreeInfo.minValue))

    bstSum = 0
    bstSize = 0

    totalSumBstNodes = leftTreeInfo.totalSumBstNodes + rightTreeInfo.totalSumBstNodes

    if isBst:
        bstSum = tree.value + leftTreeInfo.bstSum + rightTreeInfo.bstSum
        bstSize = 1 + leftTreeInfo.bstSize + rightTreeInfo.bstSize

        if bstSize >= 3:
            totalSumBstNodes = bstSum
    print(tree.value, isBst, maxValue, minValue, bstSum, bstSize, totalSumBstNodes)
    return TreeInfo(isBst, maxValue, minValue, bstSum, bstSize, totalSumBstNodes)


if __name__ == "__main__":
    data = {
        "tree": {
            "nodes": [
                {"id": "2", "left": "3", "right": "1", "value": 2},
                {"id": "1", "left": None, "right": None, "value": 1},
                {"id": "3", "left": None, "right": None, "value": 3},
            ],
            "root": "2",
        }
    }

    tree = BinaryTree(2, BinaryTree(3), BinaryTree(1))

    print(sumBsts(tree))
