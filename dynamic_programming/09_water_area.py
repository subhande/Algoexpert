# Water Area

"""
You're given an array of non-negative integers where each non-zero integer represents the height of a pillar of width 1 . Imagine water being poured over all of the pillars; write a function that returns the surface area of the water trapped between the pillars viewed from the front. Note that spilled water should be ignored.
You can refer to the first three minutes of this question's video explanation for a visual example.


Sample Input
heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]

Sample Output
48
// Below is a visual representation of the sample input.
// The dots and vertical lines represent trapped water.
// Note that the trapped water should be ignored.
//       |
//       |
// |.....|
// |.....|
// |.....|
// |..|..|
// |..|..|
// |..|..|.....|
// |..|..|.....|
//_|..|..|..||.|

Find tallest pillar to the light and right

DP Formula

water[i] = min(leftMax[i], rightMax[i]) - heights[i]

"""


# Solution 1: My Solution
# Time: O(n) | Space: O(n)
def waterArea(heights):
    leftMaxPillar = [0] * len(heights)
    rightMaxPilar = [0] * len(heights)
    leftMax = float("-inf")
    rightMax = float("-inf")
    for i in range(len(heights)):
        if heights[i] > leftMax:
            leftMaxPillar[i] = heights[i]
            leftMax = heights[i]
        else:
            leftMaxPillar[i] = leftMax

    for i in range(len(heights) - 1, -1, -1):
        print(i)
        if heights[i] > rightMax:
            rightMaxPilar[i] = heights[i]
            rightMax = heights[i]
        else:
            rightMaxPilar[i] = rightMax

    total_water = 0
    for i in range(len(heights)):
        total_water += min(leftMaxPillar[i], rightMaxPilar[i]) - heights[i]
    return total_water


# Solution 2: AlgoExpert Solution
# Time: O(n) | Space: O(n)
def waterArea(heights):
    maxes = [0 for x in heights]
    leftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, height)
    rightMax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        minHeight = min(rightMax, maxes[i])
        if height < minHeight:
            maxes[i] = minHeight - height
        else:
            maxes[i] = 0
        rightMax = max(rightMax, height)
    return sum(maxes)


# Solution 3: AlgoExpert Solution
# Time: O(n) | Space: O(1)
def waterArea(heights):
    if len(heights) == 0:
        return 0
    leftIdx = 0
    rightIdx = len(heights) - 1
    leftMax = heights[leftIdx]
    rightMax = heights[rightIdx]
    surfaceArea = 0
    while leftIdx < rightIdx:
        if heights[leftIdx] < heights[rightIdx]:
            leftIdx += 1
            leftMax = max(leftMax, heights[leftIdx])
            surfaceArea += leftMax - heights[leftIdx]
        else:
            rightIdx -= 1
            rightMax = max(rightMax, heights[rightIdx])
            surfaceArea += rightMax - heights[rightIdx]
    return surfaceArea


heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
heights = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8]
print(waterArea(heights))
