import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

primeNumberSum = 0
primeNumberMin = -1

isPrime = [ True for _ in range(N + 1) ]

isPrime[1] = False

for i in range(2, N + 1):
  if (isPrime):
    for j in range(2, (N // i) + 1):
      isPrime[i * j] = False

for i in range(M, N + 1):
  if isPrime[i]:
    primeNumberSum += i

    if primeNumberMin == -1:
      primeNumberMin = i

if primeNumberMin == -1:
  print(primeNumberMin)

else:
  print(primeNumberSum)
  print(primeNumberMin)
