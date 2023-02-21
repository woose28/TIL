import sys
import heapq

[N, M] = [int(char) for char in sys.stdin.readline().split(' ')]

mat = { (i+1): set([]) for i in range(N) }

for _ in range(M):
  [f1, f2] = [int(char) for char in sys.stdin.readline().split(' ')]

  mat[f1].add(f2)
  mat[f2].add(f1)

answer = 0
minKevin = float('inf')

for start in range(1, N + 1):
  distance = [ float('inf') for _ in range(N) ]
  visited = [ False for _ in range(N) ]

  distance[start - 1] = 0

  queue = []

  heapq.heappush(queue, (distance[start-1], start))

  while queue:
    cd, cp = heapq.heappop(queue)

    if distance[cp - 1] < cd:
      continue

    for np in mat[cp]:
      nd = cd + 1

      if nd < distance[np - 1]:
        distance[np - 1] = nd
        heapq.heappush(queue, (distance[np - 1], np))

  curKevin = sum(distance)

  if minKevin > curKevin:
    minKevin = curKevin
    answer = start

print(answer)
