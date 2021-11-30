'''
    제출 언어: Python3
    시간: 68ms
'''
import sys

def search(ss, sb, cur_idx):
    global N, ingredients, answer

    if abs(ss - sb) < answer:
        answer = abs(ss - sb)

    for i in range(cur_idx+1, N):
        cs, cb = ingredients[i]

        search(ss*cs, sb+cb, i)

    
if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    ingredients = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ]

    answer = float("inf")

    for i in range(N):
        search(ingredients[i][0], ingredients[i][1], i)

    print(answer)

