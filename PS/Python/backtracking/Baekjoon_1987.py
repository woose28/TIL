import sys

R, C = map(int, sys.stdin.readline().strip().split(' '))

mat = [ list(sys.stdin.readline()) for _ in range(R) ]

def solution(R, C, mat):
  answer = 0
  d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
  visited = [ [ set([]) for _ in range(C) ] for _ in range(R) ]

  def move(cr, cc, cs):
    nonlocal answer

    if len(cs) > answer:
      answer = len(cs)
    
    for dx, dy in d:
      nr = cr + dy
      nc = cc + dx

      if 0 <= nr < R and 0 <= nc < C and mat[nr][nc] not in cs:
        ns = ''.join(sorted(cs + mat[nr][nc]))

        if ns not in visited[nr][nc]:
          visited[nr][nc].add(ns)
          move(nr, nc, cs + mat[nr][nc])

    
  move(0, 0, mat[0][0])

  print(answer)

solution(R, C, mat)
