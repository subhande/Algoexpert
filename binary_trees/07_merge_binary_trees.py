# Merge Binary Trees

"""
Given two binary trees, merge them and return the resulting tree. If the two trees overlap during the merger, then sum the values, otherwise use the existing node.

Note that the merging process must start from the root nodes of both trees.

Sample Input

tree1 =             1    <-- root
                  /   \
                 2     3
                / \   / \
               4         7

                     
tree2 =             10    <-- root
                   /   \
                 11     12
                 / \    / \
               13  14 15  
                    

Sample Output

                11    <-- root
               /   \
             13     15
             / \    / \
            17  14 15  7
                

"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def mergeBinaryTreesHelper(tree, tree1, tree2):
    if tree1 is None and tree2 is None:
        return None
    if tree1 is not None and tree2 is not None:
        tree.value = tree1.value + tree2.value
    else:
        tree.value = tree1.value if tree2 is None else tree2.value
    tree.left = mergeBinaryTreesHelper(
        BinaryTree(None), tree1.left if tree1 else None, tree2.left if tree2 else None
    )
    tree.right = mergeBinaryTreesHelper(
        BinaryTree(None), tree1.right if tree1 else None, tree2.right if tree2 else None
    )
    return tree

# Time: O(n) | Space: O(h)
def mergeBinaryTrees(tree1, tree2):
    tree = mergeBinaryTreesHelper(BinaryTree(None), tree1, tree2)
    return tree

# Time: O(n) | Space: O(h)
def mergeBinaryTrees(tree1, tree2):
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1
    
    tree1.value += tree2.value

    tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
    tree1.right = mergeBinaryTrees(tree1.right, tree2.right)

    return tree1

# Time: O(n) | Space: O(h)
def mergeBinaryTrees(tree1, tree2):
    if tree1 is None:
        return tree2
    tree1Stack = [tree1]
    tree2Stack = [tree2]

    while len(tree1Stack) > 0:
        tree1Node = tree1Stack.pop()
        tree2Node = tree2Stack.pop()

        if tree2Node is None:
            continue

        tree1Node.value += tree2Node.value

        if tree1Node.left is None:
            tree1Node.left = tree2Node.left
        else:
            tree1Stack.append(tree1Node.left)
            tree2Stack.append(tree2Node.left)

        if tree1Node.right is None:
            tree1Node.right = tree2Node.right
        else:
            tree1Stack.append(tree1Node.right)
            tree2Stack.append(tree2Node.right)
        
    return tree1