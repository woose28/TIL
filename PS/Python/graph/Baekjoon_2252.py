import sys
from collections import deque

def solution(N, M, comparisons):
  degree = [0] * (N + 1)
  graph = [ [] for _ in range(N + 1) ]
  
  queue = deque([])
  answer = []

  for A, B in comparisons:
    graph[B].append(A)
    degree[A] += 1
  
  for i in range(1, N + 1):
    if degree[i] == 0:
      queue.append(i)
    
  while len(queue) != 0:
    student = queue.popleft()

    answer.append(student)

    for taller_student in graph[student]:
      degree[taller_student] -= 1

      if degree[taller_student] == 0:
        queue.append(taller_student)
  
  print(*answer[::-1])


if __name__ == "__main__":
  N, M = map(int, sys.stdin.readline().strip().split(' '))
  comparisons = [ list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(M) ]

  solution(N, M, comparisons)
