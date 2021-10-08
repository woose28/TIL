'''
    제출 언어: Python3
    시간: 80ms
'''
import sys

def solution(idx, num, n):
    global N, num_list, res

    if n == N:
        res.append(num)
        return

    for i in range(idx, 4):
        solution(i, num+num_list[i], n+1)

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    
    num_list = [1, 5, 10, 50]
    res = []

    solution(0, 0, 0)

    answer = len(set(res))
    print(answer)
    