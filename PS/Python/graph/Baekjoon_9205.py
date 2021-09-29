'''
    제출 언어: Python3
    시간: 116ms
'''
import sys

def solution():
    global n, spot, graph

    is_success = False
    
    visited = [ False ] * (n+2)
    visited[0] = True

    stack = [ 0 ]

    while stack:
        cur_spot = stack.pop()
        cx, cy = spot[cur_spot]

        if cur_spot == n+1:
            is_success = True
            break

        for next_spot in graph[cur_spot]:
            if not visited[next_spot]:
                visited[next_spot] = True
                stack.append(next_spot)

    return is_success


if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())

    answer = []

    for _ in range(t):
        n = int(sys.stdin.readline().strip())

        spot = []

        graph = { i: [] for i in range(n+2) }

        for _ in range(n+2):
            cx, cy = map(int, sys.stdin.readline().strip().split())

            spot.append((cx, cy))

        for i in range(n+2):
            for j in range(i+1, n+2):
                x1, y1 = spot[i]
                x2, y2 = spot[j]

                if abs(x1-x2) + abs(y1-y2) <= 1000:
                    graph[i].append(j)
                    graph[j].append(i)

        is_success = solution()

        if is_success:
            answer.append("happy")
        else:
            answer.append("sad")

    for res in answer:
        print(res)
