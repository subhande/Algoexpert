# Reverse Word in String

"""
Write a function that takes in a string of words separated by one or more whitespaces and returns a string that has these words in reverse order. For example, given the string "tim is great", your function should return "great is tim".

For this problem, a word can contain special characters, punctuation, and numbers. The words in the string will be separated by one or more whitespaces, and the reversed string must contain the same whitespaces as the original string. For example, given the string "whitespaces    4" you would be expected to return "4    whitespaces".

Note that you're not allowed to to use any built-in split or reverse methods/functions. However, you are allowed to use a built-in join method/function.

Also note that the input string isn't guaranteed to always contain words.



# Sample Input
string = "AlgoExpert is the best!"

# Sample Output
"best! the is AlgoExpert"

"""
# Time: O(n) | Space: O(n)
def reverseWordsInString(string):
    n = len(string)
    words = []
    current_word = []
    i = 0
    if string == " ":
        return " "
    while i < n:
        
        if string[i] == " ":
            whitespace_count = 0
            while i < n and string[i] == " ":
                # current_word.append(" ")
                whitespace_count += 1
                i += 1
            if whitespace_count > 1:
                current_word = [" " * (whitespace_count-1)] + current_word
            # print(words)
            # print(["".join(current_word)])
            words.append("".join(current_word))
            current_word = []
        else:
            current_word.append(string[i])
            i += 1
            if i == n:
                words.append("".join(current_word))
    if string.endswith(" "):
        return " " + " ".join(reversed(words))
    return " ".join(reversed(words))

if __name__ == "__main__":
    string = "AlgoExpert is the best!"
    print([reverseWordsInString(string)])
    string = "test        "
    out = reverseWordsInString(string)
    expected_out = "        test"
    print([len(string), len(out), len(expected_out), expected_out, out, out==expected_out])