def solution(park, routes):
    answer = []
    
    width = len(park[0])
    height = len(park)
    
    mat = [ list(row) for row in park ]
    
    startPos = []
    
    for cr, row in enumerate(mat):
        for cc, pos in enumerate(row):
            if pos == "S":
                startPos.extend([cr, cc]);
                mat[cr][cc] = "O"
                
    for route in routes:
        [direction, _distance] = route.split(' ')
        distance = int(_distance)
        
        [cr, cc] = startPos;
        
        isMovable = True
        
        if direction == "S":
            for nr in range(cr + 1, cr + distance + 1):
                if (nr >= height or mat[nr][cc] == "X"):
                    isMovable = False
                    break
            
            if isMovable:
                startPos[0] = cr + distance
            
        elif direction == "E":
            for nc in range(cc + 1, cc + distance + 1):
                if (nc >= width or mat[cr][nc] == "X"):
                    isMovable = False  
                
            if isMovable:
                startPos[1] = cc + distance
                
        elif direction == "W":
            for nc in range(cc - 1, cc - distance -1, -1):
                if (nc < 0 or mat[cr][nc] == "X"):
                    isMovable = False
                
            if isMovable:
                startPos[1] = cc - distance
                
        elif direction == "N":
            for nr in range(cr - 1, cr - distance -1, -1):
                if (nr < 0 or mat[nr][cc] == "X"):
                    isMovable = False
            
            if isMovable:
                startPos[0] = cr - distance
                    
    answer = startPos
    
    return answer