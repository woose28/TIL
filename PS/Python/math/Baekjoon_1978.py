'''
    제출 언어: Python3
    시간: 68ms
'''
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    num_list = list(map(int, sys.stdin.readline().strip().split()))
    
    max_num = max(num_list)
    is_prime_num = [ True ] * max_num
    is_prime_num[0] = False
    answer = 0

    for i in range(2, max_num+1):
        if is_prime_num[i-1]:
            j = 2

            while i * j <= max_num:
                is_prime_num[(i*j)-1] = False
                j += 1


    for i in num_list:
        if is_prime_num[i-1]:
            answer += 1

    print(answer)