'''
    제출 언어: Python3
    시간: 68ms
'''
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    e = 1
    answer = 0 

    while True:
        if N < 10 ** e:
            answer += (N - 10 ** (e - 1) + 1) * e
            break

        else:
            answer += (10 ** e - 10 ** (e - 1)) * e
            e += 1
    
    print(answer)

