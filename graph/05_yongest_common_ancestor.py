# Yongest Common Ancestor

"""
You're given three inputs, all of which are instances of an AncestralTree class that have an ancestor property pointing to their youngest ancestor. The first input is the top ancestor in an ancestral tree (i.e., the only instance that has no ancestor--its ancestor property points to None/null), and the other two inputs are descendants in the ancestral tree.

Write a function that returns the youngest common ancestor to the two descendants.

Note that a descendant is considered its own ancestor. So in the simple ancestral tree below, the youngest common ancestor to nodes A and B is node A.

// The youngest common ancestor to nodes A and B is node A.
     A
    /
   B

Sample Input
// The nodes are from the ancestral tree below.
topAncestor = node A
descendantOne = node E
descendantTwo = node I

// The ancestral tree.
        A
      /   \
     B     C
    / \   / \
    D   E F   G
   / \
  H   I


Sample Output
node B



"""
import unittest


# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getDescendantDepth(descendant):
    depth = 0
    while descendant.ancestor is not None:
        depth += 1
        descendant = descendant.ancestor
    return depth


# Brute Force Solution
# Time: O(d) | Space: O(d) - where d is the depth of the deeper descendant
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    ancestorsOne = []
    ancestorsTwo = []
    ancestorsOneDepth = 0
    ancestorsTwoDepth = 0

    ancestorsOne.append(descendantOne)
    while descendantOne.ancestor is not None:
        ancestorsOne.append(descendantOne.ancestor)
        ancestorsOneDepth += 1
        descendantOne = descendantOne.ancestor

    ancestorsTwo.append(descendantTwo)
    while descendantTwo.ancestor is not None:
        ancestorsTwo.append(descendantTwo.ancestor)
        ancestorsTwoDepth += 1
        descendantTwo = descendantTwo.ancestor
    diff = abs(ancestorsOneDepth - ancestorsTwoDepth)
    ancestorOneStartIdx = 0 if ancestorsOneDepth < ancestorsTwoDepth else diff
    ancestorTwoStartIdx = 0 if ancestorsTwoDepth < ancestorsOneDepth else diff
    while ancestorOneStartIdx < len(ancestorsOne) and ancestorTwoStartIdx < len(
        ancestorsTwo
    ):
        if (
            ancestorsOne[ancestorOneStartIdx].name
            == ancestorsTwo[ancestorTwoStartIdx].name
        ):
            return ancestorsOne[ancestorOneStartIdx]
        ancestorOneStartIdx += 1
        ancestorTwoStartIdx += 1
    return None

# Algoexpert Solution [Optimal Solution]
def getDescendantDepth(descendant):
    depth = 0
    while descendant.ancestor is not None:
        depth += 1
        descendant = descendant.ancestor
    return depth

# Time: O(d) | Space: O(1) - where d is the depth of the deeper descendant
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne)
    depthTwo = getDescendantDepth(descendantTwo)
    if depthOne > depthTwo:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)
    
def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant




class AncestralTree(AncestralTree):
    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees


def test_case_1():
    trees = new_trees()
    trees["A"].addDescendants(trees["B"], trees["C"])
    trees["B"].addDescendants(trees["D"], trees["E"])
    trees["D"].addDescendants(trees["H"], trees["I"])
    trees["C"].addDescendants(trees["F"], trees["G"])

    yca = getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"])
    assert yca == trees["B"], f"Expected {trees['B'].name}, got {yca}"





def test_case_1():
    case = {
        "nodes": [
            {"ancestor": None, "id": "A", "name": "A"},
            {"ancestor": "A", "id": "B", "name": "B"},
            {"ancestor": "A", "id": "C", "name": "C"},
            {"ancestor": "A", "id": "D", "name": "D"},
            {"ancestor": "A", "id": "E", "name": "E"},
            {"ancestor": "A", "id": "F", "name": "F"},
            {"ancestor": "B", "id": "G", "name": "G"},
            {"ancestor": "B", "id": "H", "name": "H"},
            {"ancestor": "B", "id": "I", "name": "I"},
            {"ancestor": "C", "id": "J", "name": "J"},
            {"ancestor": "D", "id": "K", "name": "K"},
            {"ancestor": "D", "id": "L", "name": "L"},
            {"ancestor": "F", "id": "M", "name": "M"},
            {"ancestor": "F", "id": "N", "name": "N"},
            {"ancestor": "H", "id": "O", "name": "O"},
            {"ancestor": "H", "id": "P", "name": "P"},
            {"ancestor": "H", "id": "Q", "name": "Q"},
            {"ancestor": "H", "id": "R", "name": "R"},
            {"ancestor": "K", "id": "S", "name": "S"},
            {"ancestor": "P", "id": "T", "name": "T"},
            {"ancestor": "P", "id": "U", "name": "U"},
            {"ancestor": "R", "id": "V", "name": "V"},
            {"ancestor": "V", "id": "W", "name": "W"},
            {"ancestor": "V", "id": "X", "name": "X"},
            {"ancestor": "V", "id": "Y", "name": "Y"},
            {"ancestor": "X", "id": "Z", "name": "Z"},
        ]
    }
    trees = new_trees()
    for node in case["nodes"]:
        if node["ancestor"] is not None:
            trees[node["id"]].ancestor = trees[node["ancestor"]]

    yca = getYoungestCommonAncestor(trees["A"], trees["A"], trees["B"])
    assert yca == trees["A"], f"Expected {trees['A'].name}, got {yca}"

test_case_1()