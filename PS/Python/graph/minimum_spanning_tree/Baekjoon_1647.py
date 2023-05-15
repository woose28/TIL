import sys

N, M = map(int, sys.stdin.readline().split(' '))

edges = [ list(map(int, sys.stdin.readline().split(' '))) for _ in range(M) ]

edges.sort(key = lambda x: x[2])

def solution(N, M, edges):
  parents = [ i for i in range(N + 1) ]
  
  def find_parent(target):
    if target == parents[target]:
      return target

    parents[target] = find_parent(parents[target])

    return parents[target]

  answer = 0
  last_index = None

  for i, (A, B, C) in enumerate(edges):
    A_parent = find_parent(A)
    B_parent = find_parent(B)

    if A_parent != B_parent:
      if A_parent < B_parent:
        parents[B_parent] = A_parent
      else:
        parents[A_parent] = B_parent
      
      last_index = i
      answer += C
  
  answer -= edges[last_index][2]

  print(answer)

solution(N, M, edges)
