'''
    제출 언어: Python3
    시간: 68ms
'''
import sys

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().strip().split())

    is_prime_num = [True] * (N+1)
    is_prime_num[0] = False
    is_prime_num[1] = False

    change_cnt = 0
    answer = 0

    for i in range(2, N+1):
        if is_prime_num[i]:
            change_cnt += 1

            if change_cnt == K:
                answer = i
                break
            
            j = 2

            while i * j <= N:
                if is_prime_num[i*j]:
                    is_prime_num[i*j] = False
                    change_cnt += 1

                if change_cnt == K:
                    answer = i * j
                    break
                
                j += 1
        
        if change_cnt == K:
            break

    
    print(answer)
