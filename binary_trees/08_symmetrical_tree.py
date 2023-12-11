# Symmtrical Tree

"""
Write a function that takes in a Binary Tree and checks if its a mirror image of itself (i.e. symmetric around its center).

A Binary Tree is symmetric if its data and shape remain unchanged when it's reflected about the root node. The following tree is an example of a symmetric Binary Tree:

Sample Input
tree =             1    <-- root




"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    return treesAreMirrored(tree.left, tree.right)

# Time: O(n) | Space: O(h)
def treesAreMirrored(left, right):
    if left is not None and right is not None and left.value == right.value:
        return treesAreMirrored(left.left, right.right) and treesAreMirrored(
            left.right, right.left
        )
    return left == right


def symmetricalTree(tree):
    stackLeft = [tree.left]
    stackRight = [tree.right]

    while len(stackLeft) > 0:
        left = stackLeft.pop()
        right = stackRight.pop()

        if left is None and right is None:
            continue

        if left is None or right is None or left.value != right.value:
            return False 

        stackLeft.append(left.left)
        stackLeft.append(left.right)
        stackRight.append(right.right)
        stackRight.append(right.left)

    return True
