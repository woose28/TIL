import sys

def findPassword(currentPassword, currentIndex, consonantCount, vowelCount):
  global L, C, alphabet, answers, vowels

  if len(currentPassword) == L:
    if consonantCount >= 2 and vowelCount >= 1:
      answers.append(currentPassword)
    
    return

  for i in range(currentIndex + 1, C):
    currentAlphabet = alphabet[i]

    if currentAlphabet in vowels:
      findPassword(currentPassword + currentAlphabet, i, consonantCount, vowelCount + 1)
    
    else:
      findPassword(currentPassword + currentAlphabet, i, consonantCount + 1, vowelCount)


L, C = map(int, sys.stdin.readline().strip().split(' '))
alphabet = sys.stdin.readline().strip().split(' ')

alphabet.sort()

answers = []

vowels = ['a', 'e', 'i', 'o', 'u']

findPassword('', -1, 0, 0)

print("\n".join(answers))
