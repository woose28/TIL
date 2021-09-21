def calculate(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    
def solution(n, s, a, b, fares):
    answer = 0
    
    dist = [ [ float('inf') ] * n for _ in range(n) ]
    
    for i in range(n):
        dist[i][i] = 0
        
    for fare in fares:
        c, d, f = fare
        
        dist[c-1][d-1] = f
        dist[d-1][c-1] = f
    
    
    calculate(n, dist)
    
    answer = dist[s-1][a-1] + dist[s-1][b-1]
    
    for i in range(n):
        answer = min(answer, dist[s-1][i-1]+dist[i-1][a-1]+dist[i-1][b-1])
    
        
    return answer