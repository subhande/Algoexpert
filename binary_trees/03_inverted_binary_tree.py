# Inverted Binary Tree

"""
Write a function that takes in a Binary Tree and inverts it. In other words, the function should swap every left node in the tree for its corresponding right node.

Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
tree =             1    <-- root
                 /   \
                2     3
               / \   / \
              4   5 6   7
             / \   \
            8   9  10

            
Sample Output
            1    <-- root
          /   \
         3     2
        / \   / \
       7   6 5   4
      / \   \ 
     10  9  8
"""

# Brute Force
# Time: O(n) | Space: O(n)
def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            return
        swapLeftAndRight(current)
        invertBinaryTree(current.left)
        invertBinaryTree(current.right)


# Optimal Approach
# Time: O(n) time | O(d) Space
def invertBinaryTree(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


