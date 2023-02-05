# Sunset View

"""
Given an array of buildings and a direction that all of the buildings face, return an array of the indices of the buildings that can see the sunset.
A building can see the sunset if it's strictly taller than all of the buildings that come after it in the direction that it faces.
The input array named buildings contains positive, non-zero integers representing the heights of the buildings. A building at index i thus has a height denoted by buildings [i]. All of the buildings face the same direction, and this direction is either east or west, denoted by the input string named direction, which will always be equal to either "EAST" or "WEST". In relation to the input array, you can interpret these directions as right for east and left for west.
Important note: the indices in the ouput array should be sorted in ascending order.

# Sample Input
buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "EAST"
# Sample Output
[1, 3, 6, 7] # the indices of the buildings that can see the sunset

"""

"""
i = 0
------
building = 3
stack = [0]
------------
i = 1
-------
building = 5
stack = [0]
5 >= 3
stack = [1]
-----------
i = 2
-------
building = 4
stack = [1]
4 >= 5
stack = [1, 2]
-----------
i = 3
-------
building = 4
stack = [1, 2]
4 >= 4
stack = [1, 3]
-----------
i = 4
-------
building = 3
stack = [1, 3]
3 >= 4
stack = [1, 3, 4]

"""
# Time: O(n) | Space: O(n)
def sunsetViews(buildings, direction):
    stack = []
    if direction == "WEST":
        buildings = buildings[::-1]
    for i, building in enumerate(buildings):
        while stack and building >= buildings[stack[-1]]:
            stack.pop()
        stack.append(i)
    if direction == "WEST":
        stack = [len(buildings) - i - 1 for i in stack]
    return sorted(stack)

