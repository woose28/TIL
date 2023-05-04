import sys

N = int(sys.stdin.readline())
edges = [ int(sys.stdin.readline()) for _ in range(N) ]

edges.sort(reverse=True)

answer = -1

for i in range(N - 2):
  if edges[i] < edges[i + 1] + edges[i + 2]:
    answer = edges[i] + edges[i + 1] + edges[i + 2]
  
    break
  
print(answer)
