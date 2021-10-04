'''
    제출 언어: PyPy3
    시간: 272ms
'''
import sys

def calculation(x, y, d1, d2):
    global N, mat, total
    
    area_list = [ [0] * N for _ in range(N) ]
    people = [0] * 5

    for i in range(0, d1+1):
        area_list[x+i][y-i] = 5
        area_list[x+d2+i][y+d2-i] = 5

    for i in range(0, d2+1):
        area_list[x+i][y+i] = 5
        area_list[x+d1+i][y-d1+i] = 5

    for i in range(0, x+d1):
        for j in range(0, y+1):
            if area_list[i][j] == 5:
                break

            people[0] += mat[i][j]

    for i in range(0, x+d2+1):
        for j in range(N-1, y, -1):
            if area_list[i][j] == 5:
                break

            people[1] += mat[i][j]

    for i in range(x+d1, N):
        for j in range(0, y-d1+d2):
            if area_list[i][j] == 5:
                break

            people[2] += mat[i][j]

    for i in range(x+d2+1, N):
        for j in range(N-1, y-d1+d2-1, -1):
            if area_list[i][j] == 5:
                break

            people[3] += mat[i][j]

    people[4] = total - (people[0]+people[1]+people[2]+people[3])

    res = max(people) - min(people)
    return res

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    mat = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ]
    total = sum([sum(row) for row in mat])

    answer = float('inf')

    for r in range(N):
        for c in range(N):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    if r + d1 + d2 <= N-1 and 0 <= c - d1 and c + d2 <= N-1:
                        answer = min(answer, calculation(r, c, d1, d2))

    print(answer)
