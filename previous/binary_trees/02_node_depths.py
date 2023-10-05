# Node Depths

"""
The distance between a node in a Binary Tree and the tree's root is called the node's depth.

Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.

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
16
            
"""



# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Brute Force Approach

# Time: O(n) | Space: O(h)
def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sumOfDepths


# Optimal Approach

# Time: O(n) | Space: O(h)
def nodeDepths(root):
    return nodeDepthsHelper(root, 0)


def nodeDepthsHelper(node, depth):
    if node is None:
        return 0
    return depth + nodeDepthsHelper(node.left, depth + 1) + nodeDepthsHelper(node.right, depth + 1)