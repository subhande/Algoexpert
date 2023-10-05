# Nth Fibonacii

# Brute Force - Recursion
# Time: O(2^n) | Space: O(n)
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)



# Optimal Approach - Simple Loop
# Time: O(n) | Space: O(1)
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0 
        b = 1
        fib = b
        for i in range(2, n):
            c = a + b
            fib = c
            a = b
            b = c
        return fib

# Optimal Approach - Memoization
# Time: O(n) | Space: O(n)
class FibDict(dict):
    def __init__(self):
        self[0] = self[1] = 0
        self[2] = 1
    def __missing__(self, k):
        fibk = self[k] = self[k-1] + self[k-2]
        return fibk
    
# Optimal Approach - Memoization
# Time: O(n) | Space: O(n)
def getNthFib(n, memoize = {1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
        return memoize[n]
    

if __name__ == "__main__":
    fib_dict = FibDict()
    for i in range(1, 10):
        a = fib_dict[i]
        b = getNthFib(i)
        print([a, b, a == b])