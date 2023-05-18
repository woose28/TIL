import sys

def solution(N, M):
  answer = 0
  parents = [ i for i in range(N) ]

  def find_parent(v):
    if parents[v] == v:
      return v

    parents[v] = find_parent(parents[v])

    return parents[v]
  
  def union(v1, v2):
    if v1 < v2:
      parents[v2] = v1
    else:
      parents[v1] = v2
  
  for i in range(M):
    v1, v2 = map(int, sys.stdin.readline().split(' '))

    v1_parent = find_parent(v1)
    v2_parent = find_parent(v2)

    if v1_parent == v2_parent:
      answer = i + 1
      break

    union(v1_parent, v2_parent)

  print(answer)

if __name__ == "__main__":
  N, M = map(int, sys.stdin.readline().split(' '))

  solution(N, M)
  