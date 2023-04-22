N = int(input())
positions = [ [ int(char) for char in input().split(' ') ] for _ in range(N) ]

sortedPositions = sorted(positions, key = lambda x: (x[1], x[0]))

for position in sortedPositions:
  print(" ".join(map(str, position)))
  