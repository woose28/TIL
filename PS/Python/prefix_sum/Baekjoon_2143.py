'''
    제출 언어: Python3
    시간: 532ms
'''
import sys
from collections import Counter

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    arr_n = list(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline().strip())
    arr_m = list(map(int, sys.stdin.readline().strip().split()))

    sum_n = [0] * (n+1)
    sum_m = [0] * (m+1)

    for i in range(n):
        sum_n[i+1] = sum_n[i] + arr_n[i]

    for i in range(m):
        sum_m[i+1] = sum_m[i] + arr_m[i]
        
    answer = 0

    part_n = []
    part_m = []

    for i in range(n):
        for j in range(i+1, n+1):
            part_n.append(sum_n[j] - sum_n[i])

    for i in range(m):
        for j in range(i+1, m+1):
            part_m.append(sum_m[j] - sum_m[i])

    counter_n = Counter(part_n)
    counter_m = Counter(part_m)

    for nk, nv in counter_n.items():
        if T - nk in counter_m:
            answer += nv * counter_m[T - nk]
    
    print(answer)

