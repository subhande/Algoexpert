# Evaluate Expression Tree

"""
You're given a binary expression tree. Write a function to evaluate this tree mathematically and return a single resulting integer.

All leaf nodes in the tree represent operands, which will always be positive integers. All of the other nodes represent operators. There are 4 operators supported, each of which is represented by a negative integer:
- -1 : Addition operator, adding the left and right subtrees.
- -2: Subtraction operator, subtracting the right subtree from the left subtree.
- -3: Division operator, dividing the left subtree by the right subtree. If the result is a decimal, it should be rounded towards zero.
- -4 : Multiplication operator, multiplying the left and right subtrees.

You can assume the tree will always be a valid expression tree. Each operator also works as a grouping symbol, meaning the bottom of the tree is always evaluated first, regardless of the operator.

Sample Input
tree =          -1
              /    \
            -2     -4
           /  \    / \
          3    4  5   6

Sample Output
-29

"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Recursive Approach
# Time: O(n) | Space: O(h) where h is the height of the tree
def evaluateExpressionTree(tree):
    operator_dict = {
        -1: lambda x, y: x + y,
        -2: lambda x, y: x - y,
        -3: lambda x, y: int(x/y),
        -4: lambda x, y: x * y,
    }
    if tree.value >= 0:
        return tree.value
        
    leftValue = evaluateExpressionTree(tree.left)
    rightValue = evaluateExpressionTree(tree.right)
    
    return operator_dict[tree.value](leftValue, rightValue)
