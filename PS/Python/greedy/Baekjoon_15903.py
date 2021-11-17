'''
    제출 언어: Python3
    시간: 84ms
'''
import sys
import heapq

def solution():
    global m, cards

    res = 0

    heapq.heapify(cards)

    for _ in range(m):
        n1 = heapq.heappop(cards)
        n2 = heapq.heappop(cards)

        heapq.heappush(cards, n1+n2)
        heapq.heappush(cards, n1+n2)

    res = sum(cards)

    return res

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split())

    cards = list(map(int, sys.stdin.readline().strip().split()))

    answer = solution()

    print(answer)


