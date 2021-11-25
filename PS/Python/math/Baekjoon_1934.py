'''
    제출 언어: Python3
    시간: 68ms
'''
import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    
    return a

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    answers = []

    for _ in range(T):
        num1, num2 = map(int, sys.stdin.readline().strip().split())

        num_gcd = gcd(num1, num2)

        answers.append((num1 * num2) // num_gcd)

    for answer in answers:
        print(answer)

    