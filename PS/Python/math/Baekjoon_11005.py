'''
    제출 언어: PyPy3
    시간: 144ms
'''
import sys

def convertTo(N, B):
    global char_list
    res = ""

    while N > 0:
        N, left = N // B, N % B
        res += char_list[left]

    return res[::-1]

if __name__ == "__main__":
    char_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    N, B = map(int, sys.stdin.readline().strip().split())

    res = convertTo(N, B)
    
    print(res)