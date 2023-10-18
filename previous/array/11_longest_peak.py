# Logest Peak
"""
Write a function that takes in an array of integers and returns the length of the longest peak in the array.
A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak), at which point they become strictly decreasing. At least three integers are required to form a peak.
For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers 1, 2, 2, 0. Similarly, the integers 1, 2, 3 don't form a peak because there aren't any strictly decreasing integers after the 3.
Sample Input
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
Sample Output
6 // 0, 10, 6, 5, -1, -3


"""

# Time: O(n) | Space O(n)
def longestPeak(array):
    logestPeakLength = 0
    isPeak = False
    peakDirection = None
    currentPeakLength = 0
    INC = "inc"
    DEC = 'dec'
    for i in range(1, len(array)):
        if isPeak is False:
            if array[i] > array[i-1]:
                isPeak = True
                currentPeakLength = 2
                peakDirection = INC
        else:
            if peakDirection == INC:
                if array[i] > array[i-1]:
                    currentPeakLength += 1
                elif array[i] < array[i-1]:
                    currentPeakLength += 1
                    peakDirection = DEC
                else:
                    isPeak = False
                    peakDirection = None
            elif peakDirection == DEC:
                if array[i] < array[i-1]:
                    currentPeakLength += 1
                else:
                    isPeak = False
                    peakDirection = None
                    if currentPeakLength >= 3:
                        logestPeakLength = max(currentPeakLength, logestPeakLength)
                    currentPeakLength = 0
                    if array[i] > array[i-1]:
                        isPeak = True
                        currentPeakLength = 2
                        peakDirection = INC
        if i == len(array) - 1 and isPeak is True and peakDirection == DEC:
            if currentPeakLength >= 3:
                logestPeakLength = max(currentPeakLength, logestPeakLength)
    return logestPeakLength

# Time: O(n) | Space O(n)
def longestPeakV2(array):
    longestPeakLength = 0
    i = 1
    while i < len(array)-1:
        isPeak = array[i-1] < array[i] and array[i] > array[i+1]
        if not isPeak:
            i += 1
            continue
        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1
        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightIdx
    return longestPeakLength

if __name__ == "__main__":
    # array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    # print(longestPeak(array))
    array = [1, 3, 2]
    print(longestPeak(array))
    array = [1, 2, 3, 3, 2, 1]
    print(longestPeak(array))