import sys

def solution():
    global n, p1, p2, relation
    visited = [ False ] * (n+1)

    stack = [ (p1, 0) ]
    visited[p1] = True

    res = -1

    while stack:
        cp, cd = stack.pop()

        if cp == p2:
            res = cd
            break

        for np in range(n+1):            
            if relation[cp][np] and not visited[np]:
                visited[np] = True
                stack.append((np, cd+1))
    
    return res
        

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    p1, p2 = map(int, sys.stdin.readline().strip().split())

    m = int(sys.stdin.readline().strip())

    relation = [ [ False ] * (n+1) for _ in range(n+1) ]

    for _ in range(m):
        r1, r2 = map(int, sys.stdin.readline().strip().split())

        relation[r1][r2] = True
        relation[r2][r1] = True

    res = solution()

    print(res)

