'''
    제출 언어: Python3
    시간: 164ms
'''
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    answer = 0

    for _ in range(N):
        word = sys.stdin.readline().strip()

        stack = []

        for i in range(len(word)):
            if len(stack) == 0:
                stack.append(word[i])

            elif stack[-1] == word[i]:
                stack.pop()

            else:
                stack.append(word[i])
        
        if len(stack) == 0:
            answer += 1
        

    print(answer)
