from collections import deque

N, K = [ int(char) for char in input().split(' ') ]
A = [ int(Ai) for Ai in input().split(' ') ]

def solution(N, A, K):
  answer = 1
  zeroCount = 0

  robots = deque([ False for _ in range(N) ])
  copiedA = deque([ Ai for Ai in A ])

  while True:
    lastA = copiedA.pop()
    copiedA.appendleft(lastA)

    robots.pop()
    robots.appendleft(False)
    robots[N - 1] = False

    if zeroCount >= K:
      break

    for i in range(N - 2, -1, -1):
      isExistedRobot = robots[i]
      isExistedRobotNext = robots[i+1]
      isMoveNext = copiedA[i+1] > 0

      if isExistedRobot and not isExistedRobotNext and isMoveNext:
        robots[i] = False
        copiedA[i+1] -= 1

        if i + 1 != N - 1:
          robots[i+1] = True

        if copiedA[i+1] == 0:
          zeroCount += 1
        pass

    if zeroCount >= K:
      break
    
    if copiedA[0] > 0:
      copiedA[0] -= 1
      robots[0] = True

      if copiedA[0] == 0:
        zeroCount += 1

    if zeroCount >= K:
      break

    answer += 1
  
  print(answer)


solution(N, A, K)
  