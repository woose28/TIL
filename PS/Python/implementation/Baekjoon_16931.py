import sys

def solution(N, M, matrix):
  answer = 0

  d = [(0, -1), (1, 0), (0, 1), (-1, 0)]

  for cr in range(N):
    for cc in range(M):
      answer += 2

      for dx, dy in d:
        nr = cr + dy
        nc = cc + dx

        if 0 <= nr < N and 0 <= nc < M:
          if matrix[cr][cc] > matrix[nr][nc]:
            answer += (matrix[cr][cc] - matrix[nr][nc])
          
        else:
          answer += matrix[cr][cc]




  print(answer)


if __name__ == "__main__":
  N, M = map(int, sys.stdin.readline().split(' '))

  matrix = [ list(map(int, sys.stdin.readline().split(' '))) for _ in range(N) ]

  solution(N, M, matrix)
