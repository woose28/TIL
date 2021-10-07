'''
    제출 언어: Python3
    시간: 516ms
'''
import heapq
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    time_list = sorted([ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ], key = lambda x: x[0])

    
    room_list = [ time_list[0][1] ]

    for i in range(1, N):
        cs, ce = time_list[i]

        if cs >= room_list[0]:
            heapq.heappop(room_list)

        heapq.heappush(room_list, ce)
        
    answer = len(room_list)
    print(answer)
