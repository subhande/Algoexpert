# Balanced Brackets

"""
Write a function that takes in a string made up of brackets ((, [, {, ), ], and }) and other optional characters. The function should return a boolean representing whether the string is balanced with regards to brackets.

A string is said to be balanced if it has as many opening brackets of a certain type as it has closing brackets of that type and if no bracket is unmatched. Note that an opening bracket can't match a corresponding closing bracket that comes before it, and similarly, a closing bracket can't match a corresponding opening bracket that comes after it. Also, brackets can't overlap each other as in [(]).

# Sample Input
string = "([])(){}(())()()"

# Sample Output
true

"""

def balancedBrackets(string):
    stack = []
    bracket_dict = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for s in string:
        if s in ["(", "[", "{"]:
            stack.append(s)
        elif s in [")", "]", "}"]:
            if not stack:
                return False
            if bracket_dict[s] != stack[-1]:
                return False
            else:
                stack.pop()
    return stack == []
    
if __name__ == "__main__":
    input__ = ["([])(){}(())()()"]
    expected_output__ = True
    output = balancedBrackets(*input__)
    print(output)


