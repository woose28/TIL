'''
    제출 언어: Python3
    시간: 100ms
'''
import sys 

def calculate(unit):
    global num_list

    res = 0

    for num in num_list:
        res += num // unit

    return res

def search():
    global max_num, N
    left, right = 1, max_num

    while left < right:
        mid = (left+right) // 2

        if calculate(mid) >= N:
            left = mid + 1
        else:
            right = mid

    return right - 1

if __name__ == "__main__":
    K, N = map(int, sys.stdin.readline().strip().split())

    num_list = [ int(sys.stdin.readline().strip()) for _ in range(K) ]

    num_list.sort()    
    max_num = num_list[-1]

    answer = None

    if K == N and len(set(num_list)) == 1:
        answer = num_list[-1]
    
    else:
        answer = search()

    print(answer)
