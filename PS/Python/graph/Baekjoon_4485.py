import sys
import heapq

d = [(0, -1), (1, 0), (0 ,1), (-1, 0)]

answers = []

while True:
  N = int(sys.stdin.readline())

  if N == 0:
    break

  mat = [ list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N) ]
  visited = [ [ float('inf') ] * N for _ in range(N) ]

  queue = [(mat[0][0], 0, 0)]
  visited[0][0] = mat[0][0]

  while queue:
    cm, cr, cc = heapq.heappop(queue)

    for dx, dy in d:
      nr = cr + dy
      nc = cc + dx
      
      if 0 <= nr < N and 0 <= nc < N:
        nm = cm + mat[nr][nc]
        
        if visited[nr][nc] > nm:
          visited[nr][nc] = nm
          heapq.heappush(queue, (nm, nr, nc))

  answers.append(visited[N - 1][N - 1])
  

for index, answer in enumerate(answers):
  print(f"Problem {index + 1}: {answer}")
  
