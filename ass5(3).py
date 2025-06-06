def nextword(w):
    w = list(w)
    i = len(w) - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i=i-1
    if i == -1:
        return "No next permutation"
    j = len(w) - 1
    while w[j] <= w[i]:
        j=j-1
    w[i], w[j] = w[j], w[i]
    w = w[:i + 1] + w[i + 1:][::-1]
    return ''.join(w)
word = input("enter a word")
result = nextword(word)
print(result)
