import sys

N = int(sys.stdin.readline())
words = set([ sys.stdin.readline().strip() for _ in range(N) ])

sortedWords = sorted(words, key = lambda x: (len(x), x))

print("\n".join(sortedWords))
