# BST Construction


"""
Write a BST class for a Binary Search Tree. The class should support:
- Inserting values with the insert method.
- Removing values with the remove method; this method should only remove the first instance of a given value.
- Searching for values with the contains method.

Note that you can't remove values from a single-node tree. In other words, calling the remove method on a single-node tree should simply not do anything.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.

Sample Input
tree =            10
                /    \
               5      15
              / \    /  \
             2   5  13  22
            /        \
           1          14
tree.insert(12)
tree.remove(10)
tree.contains(15)


"""  # Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.



# Recusive
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space
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
        return self

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True
        
    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def remove(self, value, parent=None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right
        return self

# Looping
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            elif value > currentNode.value:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        
        return self

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False


    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self


if __name__ == "__main__":
    # import program
    import unittest

    # BST = program.BST

    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)

    root.insert(12)
    assert root.right.left.left.value == 12

    root.remove(10)
    assert not root.contains(10)
    assert root.value == 12

    assert root.contains(15)
            
