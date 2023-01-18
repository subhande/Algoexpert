# Semordnilap

"""
Write a function that takes in a list of unique strings and returns a list of semordnilap pairs.

A semordnilap pair is defined as a set of different strings where the reverse of one word is the same as the forward version of the other. For example the words "diaper" and "repaid" are a semordnilap pair, as are the words "palindromes" and "semordnilap".


The order of the returned pairs and the order of the strings within each pair does not matter. 

# Sample Input
words = ["diaper", "abc", "test", "cba", "repaid"]

# Sample Output
[["diaper", "repaid"], ["abc", "cba"]]

"""
# Time: O(n * m) | Space: O(n * m) - where n is the number of words and m is the length of the longest word
def semordnilap(words):
    semordnilap_pairs_freq = {}
    semordnilap_pairs = []
    for word in words:
        reversed_word = word[::-1]
        if word == reversed_word:
            continue
        if reversed_word in words:
            if word in semordnilap_pairs_freq:
                continue
            semordnilap_pairs_freq[reversed_word] = word
            semordnilap_pairs.append([word, reversed_word])
    return semordnilap_pairs

# Time: O(n * m) | Space: O(n * m) - where n is the number of words and m is the length of the longest word
def semordnilap(words):
    wordset = set(words)
    semordnilap_pairs = []

    for word in words:
        reversed_word = word[::-1]
        if reversed_word in wordset and reversed_word != word:
            semordnilap_pairs.append([word, reversed_word])
            wordset.remove(word)
            wordset.remove(reversed_word)
    return semordnilap_pairs


if __name__ == "__main__":
    words = ["diaper", "abc", "test", "cba", "repaid"]
    words = ["aaa", "bbbb"]
    print(semordnilap(words))