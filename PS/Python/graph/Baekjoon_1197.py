import sys

V, E = map(int, sys.stdin.readline().split(' '))
edges = [ list(map(int, sys.stdin.readline().split(' '))) for _ in range(E) ]
edges.sort(key = lambda x: x[2])

def solution(V, E, edges):
  answer = 0

  parents = [ i for i in range(V + 1) ]

  def find_parent(target):
    if parents[target] == target:
      return target

    parents[target] = find_parent(parents[target])
    
    return parents[target]

  def union_parent(V1, V2):
    V1_parent = find_parent(V1)
    V2_parent = find_parent(V2)

    if V1_parent < V2_parent:
      parents[V2_parent] = V1_parent
    else:
      parents[V1_parent] = V2_parent


  for A, B, C in edges:
    A_parent = find_parent(A)
    B_parent = find_parent(B)

    if A_parent != B_parent:
      union_parent(A, B)
      answer += C
  
  print(answer)

solution(V, E, edges)
