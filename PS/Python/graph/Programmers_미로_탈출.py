from collections import deque

def bfs(maps, sr, sc, tr, tc):
    moveCount = 0
    
    rowCount = len(maps)
    colCount = len(maps[0])
    
    d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    visited = [ [False] * colCount for _ in range(rowCount)]
    
    queue = deque([(sr, sc, 0)])
    
    visited[sr][sc] = True
    
    while queue:
        cr, cc, ct = queue.popleft()
        
        if cr == tr and cc == tc:
            moveCount = ct
            break
        
        for dx, dy in d:
            nr = cr + dy
            nc = cc + dx
            
            if 0 <= nr < rowCount and 0 <= nc < colCount and maps[nr][nc] != 'X' and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, ct + 1))
        
    return moveCount
    

def solution(maps):
    answer = 0
    
    rowCount = len(maps)
    colCount = len(maps[0])
    
    parsedMap = []
    
    startPos = []
    leverPos = []
    exitPos = []
    
    for i, row in enumerate(maps):
        parsedRow = []
        
        for j, spot in enumerate(row):
            parsedRow.append(spot)
            
            if spot == "S":
                startPos = [i, j]
            
            elif spot == "E":
                exitPos = [i, j]
            
            elif spot == "L":
                leverPos = [i, j]
        
        parsedMap.append(parsedRow)
    
    moveToLeverCount = bfs(parsedMap, startPos[0], startPos[1], leverPos[0], leverPos[1])
    moveToExitCount = bfs(parsedMap, leverPos[0], leverPos[1], exitPos[0], exitPos[1])
    
    answer = moveToLeverCount + moveToExitCount
    
    if moveToLeverCount == 0 or moveToExitCount == 0:
        answer = -1
    
    return answer