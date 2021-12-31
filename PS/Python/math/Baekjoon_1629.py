'''
    제출 언어: Python3
    시간: 64ms
'''
import sys

def multiply(cur_num, target_expo, cur_expo):
    global A, B, C

    if cur_expo == target_expo:
        return cur_num % C

    elif cur_expo * 2 <= target_expo:
        return multiply((cur_num * cur_num) % C, target_expo, cur_expo * 2)

    else:
        return (cur_num * multiply(A, target_expo - cur_expo, 1)) % C


if __name__ == "__main__":
    A, B, C = map(int, sys.stdin.readline().strip().split())

    print(multiply(A, B, 1))
