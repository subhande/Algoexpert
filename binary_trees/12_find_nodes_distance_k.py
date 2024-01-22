# Find Nodes Distance K

"""
You're given the root node of a Binary Tree, a target value of a node that's contained in the tree, and a positive integer k. Write a function that returns the values of all the nodes that are exactly distance k from the node with target value.

The distance between two nodes is defined as the number of edges that must be traversed to go from one node to the other. For example, the distance between a node and its immediate left or right child is 1. The same holds in reverse: the distance between a node and its parent is 1. In a tree of three nodes where the root node has a left and right child, the left and right children are distance 2 from each other.

Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.
Note that all BinaryTree node values will be unique, and your function can return the output values in any order.

# Sample Input

# tree = 1
#     / \
#    2   3
#  / \   / \
# 4   5 6   7
#    / \
#   8   9
# target = 3
# k = 2

# Sample Output
# [2, 7, 8] // These values could be ordered differently.


PreOrder = [1, 2, 4, 5, 3, 6, 8, 7, 9]
InOrder = [4, 2, 5, 1, 8, 6, 9, 7, 3]
PostOrder = [4, 5, 2, 8, 9, 6, 7, 3, 1]


"""

# Approach 1: Treat as Graph Problem

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findParent(node, parents, parent=None):
    if node is not None:
        parents[node.value] = parent
        findParent(node.left, parents, node)
        findParent(node.right, parents, node)


def findTargetNode(tree, target, parents):
    if tree.value == target:
        return tree
    parent = parents[target]
    if parent.left and parent.left.value == target:
        return parent.left
    return parent.right

# Time Complexity: O(n) | Space Complexity: O(n)
def findNodesDistanceK(tree, target, k):
    parents = {}
    findParent(tree, parents)
    targetNode = findTargetNode(tree, target, parents)
    queue = [(targetNode, 0)]
    visited = {targetNode.value}
    while queue:
        node, distance = queue.pop(0)
        if distance == k:
            nodeDistanceK = [__node.value for __node, _ in queue]
            nodeDistanceK += [node.value]
            return nodeDistanceK
        if node.left and node.left.value not in visited:
            visited.add(node.left.value)
            queue.append((node.left, distance + 1))
        if node.right and node.right.value not in visited:
            visited.add(node.right.value)
            queue.append((node.right, distance + 1))
        if node.value in parents and parents[node.value] is not None and parents[node.value].value not in visited:
            visited.add(parents[node.value].value)
            queue.append((parents[node.value], distance + 1))
    return []


# Approach 2: Treat as Tree Problem
# TODO: Implement this approach


