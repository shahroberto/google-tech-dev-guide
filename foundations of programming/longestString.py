"""Find the longest word from D that is a subsequence of S."""


def matchWord(S, word):
    """Check if words match."""
    newS = S
    W = []
    for char in word:
        if char in newS:
            W.append(char)
            newS = newS[newS.find(char):len(newS)]
    W = ''.join(W)
    if W == word:
        return W
    else:
        return False


S = "abppplee"
D = ["able", "ale", "apple", "bale", "kangaroo"]
W = []
for word in D:
    if len(word) > len(W):
        newW = matchWord(S, word)
        if newW:
            if len(W) < len(newW):
                W = newW

print("And the winner is " + str(W))
