# Min Max Stack Construction

"""
Write a MinMaxStack class for a Min Max Stack. The class should support:
- Pushing and popping values on and off the stack.
- Peeking at the value at the top of the stack.
- Getting both the minimum and the maximum values in the stack at any given point in time.
All class methods, when considered independently, should run in constant time and with constant space.

# Sample Input
minMaxStack = MinMaxStack()
minMaxStack.push(5)
minMaxStack.push(7)
minMaxStack.push(2)
minMaxStack.getMin() # 2
minMaxStack.getMax() # 7
minMaxStack.pop()
minMaxStack.peek() # 7

# Sample Output
2
7
7
"""

# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def push(self, number):
        return self.stack.append(number)

    def getMin(self):
        return min(self.stack)

    def getMax(self):
        return max(self.stack)
