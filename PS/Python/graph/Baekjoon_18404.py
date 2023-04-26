from collections import deque

N, M = map(int, input().split(' '))
_kx, _ky = map(int, input().split(' '))
kx = _kx - 1
ky = _ky - 1

answer = []

d = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

mat = [ [False] * N for _ in range(N) ]

queue = deque([[kx, ky, 0]])
mat[kx][ky] = 0

while len(queue):
  [cx, cy, cm] = queue.popleft()

  for dx, dy in d:
    nx = cx + dx
    ny = cy + dy

    if 0 <= nx < N and 0 <= ny < N and not mat[nx][ny]:
      mat[nx][ny] = cm + 1
      queue.append([nx, ny, cm + 1])
  
for _ in range(M):
  _ex, _ey = map(int, input().split(' '))
  ex = _ex - 1
  ey = _ey - 1

  answer.append(str(mat[ex][ey]))

print(' '.join(answer))
