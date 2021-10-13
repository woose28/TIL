'''
    제출 언어: Python3
    시간: 96ms
'''
import sys

def calculate(upper_limit):
    global num_list
    
    cur_tot = 0

    for budget in num_list:
        cur_tot += min(budget, upper_limit)
    
    return cur_tot

def solution():
    global N, num_list, tot

    left, right = 1, num_list[-1]

    res = 1

    while left <= right:
        mid = (left + right) // 2

        if calculate(mid) <= tot:
            res = mid
            left = mid + 1
            
        else:
            right = mid - 1
    
    return res

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    num_list = list(map(int, sys.stdin.readline().strip().split()))
    num_list.sort()
    tot = int(sys.stdin.readline().strip())
    
    answer = solution()

    print(answer)

