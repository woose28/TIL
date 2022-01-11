'''
    제출 언어: Python3
    시간: 3040ms
'''
import sys

def binary_search(target):
    global dp

    left = 0
    right = len(dp) - 1

    while left <= right:
        mid = (left + right) // 2

        if dp[mid] < target:
            left = mid + 1

        else:
            right = mid - 1
    
    return left


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    num_list = list(map(int, sys.stdin.readline().strip().split()))

    dp = [ num_list[0] ]

    for i in range(1, N):
        if dp[-1] < num_list[i]:
            dp.append(num_list[i])
        
        else:
            pos = binary_search(num_list[i])
            dp[pos] = num_list[i]

    print(len(dp))

