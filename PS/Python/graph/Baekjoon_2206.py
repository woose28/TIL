import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split(' ')))

mat = [ list(map(int, sys.stdin.readline().strip())) for _ in range(N) ]

visited = [ [ [False] * 2 for _ in range(M) ] for _ in range(N) ]

queue = deque([(0, 0, 1, False)])

visited[0][0][0] = True
visited[0][0][1] = True

d = [(0, -1), (1, 0), (0, 1), (-1, 0)]

answer = -1

while queue:
  [cr, cc, cd, cb] = queue.popleft()

  if cr == N - 1 and cc == M - 1:
    answer = cd
    break

  for (dx, dy) in d:
    nr = cr + dy
    nc = cc + dx

    if 0 <= nr < N and 0 <= nc < M:
      if cb and not visited[nr][nc][1] and mat[nr][nc] == 0:
        queue.append((nr, nc, cd + 1, cb))
        visited[nr][nc][1] = True

      if not cb and not visited[nr][nc][0]:
        if mat[nr][nc] == 1 and not visited[nr][nc][1]:
          queue.append((nr, nc, cd + 1, True))
          visited[nr][nc][1] = True
        
        elif mat[nr][nc] == 0:
          queue.append((nr, nc, cd + 1, cb))
          visited[nr][nc][0] = True
          visited[nr][nc][1] = True

        
print(answer)