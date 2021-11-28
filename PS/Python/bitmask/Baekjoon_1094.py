'''
    제출 언어: Python3
    시간: 72ms
'''
import sys
import heapq

if __name__ == "__main__":
    X = int(sys.stdin.readline().strip())

    num_list = [64]
    
    while sum(num_list) > X:
        min_num = heapq.heappop(num_list)

        half_num = min_num // 2

        if half_num + sum(num_list) >= X:
            heapq.heappush(num_list, half_num)
        
        else:
            heapq.heappush(num_list, half_num)
            heapq.heappush(num_list, half_num)

    answer = len(num_list)

    print(answer)

