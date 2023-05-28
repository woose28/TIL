import sys

def solution(N, mat):
  answer = [ [0] * N for _ in range(N) ]

  d = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

  for cr in range(N):
    for cc in range(N):
      cur_mine = mat[cr][cc]

      if cur_mine != ".":
        answer[cr][cc] = "*"

        for dx, dy in d:
          nr = cr + dy
          nc = cc + dx

          if 0 <= nr < N and 0 <= nc < N and answer[nr][nc] != '*' and answer[nr][nc] != "M":
            nm = int(answer[nr][nc]) + int(cur_mine)

            if nm >= 10:
              answer[nr][nc] = "M"
            
            else:
              answer[nr][nc] = nm
  
  for row in answer:
    print("".join(map(str, row)))


if __name__ == "__main__":
  N = int(sys.stdin.readline().strip())

  mat = [ list(sys.stdin.readline().strip()) for _ in range(N) ]

  solution(N, mat)
